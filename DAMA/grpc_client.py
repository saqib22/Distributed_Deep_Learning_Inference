# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC grpc_service.DAMA client."""

from __future__ import print_function
import logging
from os import device_encoding

from google.protobuf.descriptor import ServiceDescriptor

import grpc
import json
import pickle
from threading import Thread, Lock

import grpc_service_pb2
import grpc_service_pb2_grpc

import numpy as np
import torch
import gzip

import random
import collections

import model.CNN as nn


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class End_Device():
    def __init__(self, device_id, server_addrs) -> None:
        self.device_id = device_id
        self.server_handles = {}
        self.server_ids = []
        self.stubs = []
        self.profits = {}
        self.server_prices = []
        self.assignment_vector = {}
        self.epsilon = 5
        # self.benefit = {
        #     "a": {
        #         "Server:50051": 23,
        #         "Server:50052": 29
        #     },
        #     "b": {
        #         "Server:50051": 15,
        #         "Server:50052": 30
        #     },
        #     "c": {
        #         "Server:50051": 20,
        #         "Server:50052": 5
        #     },
        #     "d": {
        #         "Server:50051": 15,
        #         "Server:50052": 7
        #     },
        #     "e": {
        #         "Server:50051": 11,
        #         "Server:50052": 9
        #     },
        #     "f": {
        #         "Server:50051": 5,
        #         "Server:50052": 16
        #     }
        # }
        # self.layers = ['a','b','c', 'd','e','f']
        self.layers = []
        self.benefit = collections.defaultdict(dict)
        self.authenticate(server_addrs)
        self.initialize_servers()
    
    def Diff(self, li1, li2):
        return (np.array(li1) - np.array(li2)).tolist()

    def second_best(self, li):
        return np.sort(li)[-1] if len(li) == 1 else np.sort(li)[-2]

    def initialize_servers(self):
        for stub in self.stubs:
            self.server_prices.append(stub.get_server_price(grpc_service_pb2.Price()).price_value)
            serverID = stub.get_server_id(grpc_service_pb2.ServerID()).server_id
            self.server_handles[serverID] = stub
            self.server_ids.append(serverID)
        
        print("DEBUG")
        print(self.server_prices)
    
    def authenticate(self, server_addr_list):
        for addr in server_addr_list:
            options=[
                 ('grpc.max_send_message_length', 1024*1024*1024),
                ('grpc.max_receive_message_length', 1024*1024*1024),
             ]
            channel = grpc.insecure_channel(addr, options=options)
            self.stubs.append(grpc_service_pb2_grpc.DAMAStub(channel))
    
    def start_bidding(self):
        for layer in self.layers:
            aij = list(self.benefit[layer].values())
            print(aij)
            
            # Find the best object having maximum gain
            gain = self.Diff(aij, self.server_prices)
            ji = gain.index(max(gain))
            vi = max(gain)
            wi = self.second_best(gain)
            
            print(gain)
            
            # Calculate the bid for that object
            bid = self.server_prices[ji] + vi - wi + self.epsilon
            print(bid)

            response = self.server_handles[self.server_ids[ji]].bid_server(grpc_service_pb2.Bid(bid_value = bid, device_id=self.device_id, 
                                                    benefit=aij[ji], layer=layer))

            self.server_prices[ji] = response.price_value
            print("Server Response: ", response)
            
            if response.Ack == True:
                self.profits[layer] = aij[ji] - self.server_prices[ji]
                self.assignment_vector[layer] = self.server_ids[ji]
                print("Offload layer to server")
                print(self.profits)

        for server in self.server_ids:
            response = self.server_handles[server].set_layers_assigned(grpc_service_pb2.Assignment(layers_assigned=True,
                                                                layer_profits = json.dumps(self.profits),
                                                                layer_benefits = json.dumps(self.benefit),
                                                                device_id = self.device_id
                                                                ))
            if response: continue 
            else: raise Exception ("Server response for layer assignment boolean was negative!!!")
        
        print("Discounting for layers starts")
        print("Current assignment of layers!")
        print(self.assignment_vector)

        self.mutex = Lock()
        for server in self.server_ids:
            t = Thread(target=self.discount, args=(server,))
            t.start()
            t.join()

        print("Assignment after discounts for layers")
        print(self.assignment_vector)

    def discount(self, server_id):
        response = self.server_handles[server_id].start_discounting(grpc_service_pb2.Connection())
        if response.success == False:
            print("The server " + server_id +  " has already reached the minimum assignment nkminus!!")
            return

        self.mutex.acquire()

        print("discount and bid_value sent by the server " + str(response.bid_value))

        if (response.bid_value - self.profits[response.layer]) >= self.epsilon:
            print("Discount offered to " + server_id + " for layer " + response.layer)
            self.profits[response.layer] = response.bid_value
            
            r2 = self.server_handles[server_id].ack_layer(grpc_service_pb2.AddDropLayer(layer=response.layer, profit=response.bid_value, benefit=self.benefit[response.layer][server_id]))
            r1 = self.server_handles[self.assignment_vector[response.layer]].return_layer(grpc_service_pb2.AddDropLayer(layer=response.layer, profit=response.bid_value, benefit=self.benefit[response.layer][server_id]))
            
            self.assignment_vector[response.layer] = server_id
        else:
            print("Discount not offered to " + server_id)
            r3 = self.server_handles[server_id].nack_layer(grpc_service_pb2.AddDropLayer(layer=response.layer, profit=response.bid_value, benefit=self.benefit[response.layer][server_id]))

        self.mutex.release()
    
    def initialize_task(self, input_data, model):
        self.model = model
        self.input_data = input_data
        for name, module in model.named_modules():
            if name == '' or name =='pool': continue
            self.layers.append(name)
        #Benefit calculation -> for the time being its random
        for layer in self.layers:
            for server in self.server_ids:
                self.benefit[layer][server] = random.randint(1,20)
        print("**********Benefits***********")
        print(self.benefit)
    
    def inference(self):
        print("\nStart inferencing")

        # for i, layer in enumerate(self.layers):
        #     infer_req = {}
        #     if i == 0:
        infer_req = dict()
        input_features = self.input_data.cpu().detach().numpy()
        pool_layer = getattr(self.model, 'pool')
        flatten, first_linear = False, True
        for i, (layer, server) in enumerate(self.assignment_vector.items()):
            if i == 0 or server == prev_server:
                # infer_req[layer] = {layer: pickle.dumps(getattr(self.model, layer))}
                
                layer_obj = getattr(self.model, layer)
                if isinstance(layer_obj, torch.nn.modules.linear.Linear) and first_linear:
                    flatten, first_linear = True, False
                infer_req[layer] = {layer: layer_obj}
                prev_server = server
                continue
            else:
                if len(infer_req) != 0:
                    print("\nInfer req", infer_req.keys())
                    print("Infer_req", len(infer_req))
                    print("Server: ", prev_server)
                    
                    features = self.server_handles[prev_server].infer_layer(grpc_service_pb2.Features(
                                                                        inputs = json.dumps(input_features, cls=NumpyEncoder),
                                                                        DAG = pickle.dumps(infer_req),
                                                                        pool_layer = pickle.dumps(pool_layer),
                                                                        flatten=flatten
                                                                    ))

                    input_features = np.array(json.loads(features.output)[features.layer])
                    
                    infer_req = dict()
                    infer_req[layer] = {layer: getattr(self.model, layer)}
                    prev_server = server
                    flatten = False
                else:
                    print("Inference task finished successfully !!")
        
        #Last Layer
        if len(infer_req) != 0:
            print("\nInfer req", infer_req.keys())
            print("Infer_req", len(infer_req))
            print("Server: ", prev_server)
            features = self.server_handles[prev_server].infer_layer(grpc_service_pb2.Features(
                                                                inputs = json.dumps(input_features, cls=NumpyEncoder),
                                                                DAG = pickle.dumps(infer_req),
                                                            ))
            input_features = np.array(json.loads(features.output)[features.layer])
            

        predictions = np.argmax(input_features, axis=1)
        print(predictions.shape)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel1 = grpc.insecure_channel('localhost:50051')
    channel2 = grpc.insecure_channel('localhost:50052')
    stub1 = grpc_service_pb2_grpc.DAMAStub(channel1)
    stub2 = grpc_service_pb2_grpc.DAMAStub(channel2)

    I = ['a', 'b', 'c'] # Persons
    A = ['x', 'y'] # Objects

    S = {} # Assignment vector
    
    #Prices of edge servers
    price1 = stub1.get_server_price(grpc_service_pb2.Price())
    price2 = stub2.get_server_price(grpc_service_pb2.Price())

    prices = np.array([price1.price_value, price2.price_value]) # Price vector
    
    profits = {}

    benefit = {
        "a": np.array([23, 29]),
        "b": np.array([15,30]),
        "c": np.array([20,5])
    }
    epsilon = 5
    
    device_ID = "Client:1"

    for person in I:
        aij = benefit[person]
        
        # Find the best object having maximum gain
        ji = np.argmax(aij - prices)
        vi = max(aij - prices)
        wi = np.sort(aij - prices)[-2]
        
        print(aij - prices)
        
        # Calculate the bid for that object
        bid = prices[ji] + vi - wi + epsilon
        print(bid)

        response = stub1.bid_server(grpc_service_pb2.Bid(bid_value = bid, device_id=device_ID, 
                                                benefit=aij[ji], layer=person))

        prices[ji] = response.price_value
        print("Server Response: ", response)
        
        if response.Ack == True:
            profits[response.server_id] = aij[ji] - prices[ji]
            print("Offload layer to server")
            print(profits)

        response = stub1.set_layers_assigned(grpc_service_pb2.Assignment(layers_assigned=True))
        print("Discounting for layers starts")
        print(response)
        break

if __name__ == '__main__':
    logging.basicConfig()
    #run()
    
    device = End_Device("Client:1", ['localhost:50051', 'localhost:50052'])
    
    #Deep Learning task
    model = nn.CNN(nn.NUM_CLASSES)

    state = torch.load('model/cnn.pth')
    model.load_state_dict(state)

    input_features, _ = nn.next_batch(train=False)

    device.initialize_task(input_features, model)
    
    device.start_bidding()

    device.inference()
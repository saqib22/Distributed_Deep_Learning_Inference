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

import grpc_service_pb2
import grpc_service_pb2_grpc

import numpy as np

class End_Device():
    def __init__(self, device_id, server_addrs) -> None:
        self.device_id = device_id
        self.server_ids = []
        self.stubs = []
        self.profits = {}
        self.server_prices = []
        self.assignment_vector = {}
        self.epsilon = 5
        self.benefit = {
            "a": np.array([23, 29]),
            "b": np.array([15,30]),
            "c": np.array([20,5])
        }
        self.layers = ['a','b','c']

        self.authenticate(server_addrs)
        self.initialize_servers()

    def second_best(self, li):
        return np.sort(li)[-1] if len(li) == 1 else np.sort(li)[-2]

    def initialize_servers(self):
        for stub in self.stubs:
            self.server_prices.append(stub.get_server_price(grpc_service_pb2.Price()).price_value)
            self.server_ids.append(stub.get_server_id(grpc_service_pb2.ServerID()).server_id)
    
    def authenticate(self, server_addr_list):
        for addr in server_addr_list:
            channel = grpc.insecure_channel(addr)
            self.stubs.append(grpc_service_pb2_grpc.DAMAStub(channel))

    def start_bidding(self):
        for layer in self.layers:
            aij = self.benefit[layer]
            
            # Find the best object having maximum gain
            ji = np.argmax(aij - self.server_prices)
            vi = max(aij - self.server_prices)
            wi = self.second_best(aij - self.server_prices)
            
            print(aij - self.prices)
            
            # Calculate the bid for that object
            bid = self.prices[ji] + vi - wi + self.epsilon
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
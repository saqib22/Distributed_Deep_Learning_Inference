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
"""The Python implementation of the GRPC grpc_service.DAMA server."""

from concurrent import futures
import logging

import grpc
import json

import grpc_service_pb2
import grpc_service_pb2_grpc

import sys
import numpy as np

class DAMA(grpc_service_pb2_grpc.DAMAServicer):

    def __init__(self, server_id):
        self.server_id = server_id
        self.price = 0
        self.profit = {}
        self.n_plus = 4 # upper bound on the number of layers
        self.n_minus = 2 # lower bound on the number of layers
        self.jk = {} # layers accepted by the server with their gains = benefit - profit
        self.layer_benefits = {}
        self.epsilon = 5
        self.all_layers_assigned = False

    def Diff(self, li1, li2):
        return list(np.array(li1) - np.array(li2))

    def second_best(self, li):
        return 0 if len(li) == 1 else np.sort(li)[-2]

    def get_server_price(self, request, context):
        return grpc_service_pb2.Price(price_value=self.price)
    
    def get_server_id(self, request, context):
        return grpc_service_pb2.ServerID(server_id = self.server_id)

    def return_layer(self, request, context):
        del self.jk[request.layer]
        del self.profit[request.layer]
        del self.layer_benefits[request.layer]
        self.all_layers_profits[request.layer] = request.profit
        self.all_layers_benefits[request.layer] = request.benefit
        return grpc_service_pb2.ServerResponse(success=True)

    def ack_layer(self, request, context):
        self.all_layers_profits[request.layer] = request.profit
        self.profit[request.layer] = request.profit
        self.jk[request.layer] = request.benefit - request.profit
        self.layer_benefits[request.layer] = request.benefit
        self.price = request.benefit - self.profit[request.layer]
        if len(self.jk) == self.n_plus:
            self.price = min(self.Diff(list(self.layer_benefits.values()) - list(self.profit.values())))
        return grpc_service_pb2.ServerResponse(success=True)
    
    def nack_layer(self, request, context):
        self.all_layers_profits[request.layer] = request.profit
        self.all_layers_benefits[request.layer] = request.benefit
        return grpc_service_pb2.ServerResponse(success=True)

    def start_discounting(self, request, context):
        if len(self.jk) < self.n_minus:
            max_gain_layer_value = max(self.Diff(list(self.all_layers_benefits.values()), list(self.all_layers_profits.values())))
            max_gain_layer = list(self.all_layers.keys())[list(self.all_layers.values()).index(max_gain_layer_value)]
            second_max_layer_value = self.second_best(self.Diff(list(self.all_layers_benefits.values()), list(self.all_layers_profits.values())))
            server_bid = self.all_layers_profits[max_gain_layer] + max_gain_layer_value - second_max_layer_value + self.epsilon
            return grpc_service_pb2.Bid(
                device_id = self.server_id,
                bid_value = server_bid,
                layer = max_gain_layer,
                benefit = self.all_layers_benefits[max_gain_layer],
                success=True)
        else:
            return grpc_service_pb2.Bid(success = False)

    def set_layers_assigned(self, request, context):
        if request.layers_assigned == True:
            self.all_layers_profits = json.loads(request.layer_profits)
            benefits_json = json.loads(request.layer_benefits)
            self.all_layers = {}
            self.all_layers_benefits = {}
            for i, (key, value) in enumerate(benefits_json.items()):
                self.all_layers[key] = value[self.server_id] - self.all_layers_profits[key]
                self.all_layers_benefits[key] = value[self.server_id]
            #Remove all the layers already offloaded to this server
            for key, item in self.jk.items():
                del self.all_layers_profits[key]
                del self.all_layers_benefits[key]
                del self.all_layers[key]
            
            print("*************** " + self.server_id + "***************")
            print("All layers assigned for the device " + request.device_id)
            print("Layers associated with this device (before discounting) are " +str(self.jk) +"\n\n")
            return grpc_service_pb2.ServerResponse(success=True)

    def bid_server(self, request, context):
        if len(self.jk) < self.n_plus:
            self.profit[request.layer] = request.benefit - request.bid_value
            self.jk[request.layer] = request.benefit - self.profit[request.layer]
            self.layer_benefits[request.layer] = request.benefit
            # self.price = request.benefit - self.profit[request.layer]
            if len(self.jk) == self.n_plus:
                self.price = min(self.Diff(list(self.layer_benefits.values()), list(self.profit.values())))
            return grpc_service_pb2.BiddingResult(server_id=self.server_id, 
                                                   Ack=True, 
                                                   price_value=self.price)
        
        elif request.bid_value >= self.price + self.epsilon:
            min_gain_layer_value = min(self.Diff(list(self.layer_benefits.values()), list(self.profit.values())))
            min_gain_layer = list(self.jk.keys())[list(self.jk.values()).index(min_gain_layer_value)]
            self.profit[request.layer] = request.benefit - request.bid_value
            self.price = min_gain_layer_value
            return grpc_service_pb2.BiddingResult(server_id=self.server_id, 
                                                   Ack=True,
                                                   price_value=self.price,
                                                   Nack_layer=min_gain_layer)
        

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_service_pb2_grpc.add_DAMAServicer_to_server(DAMA('Server:' + port), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve(port=sys.argv[1])
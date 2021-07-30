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
        self.jk = [] # layers accepted by the server
        self.layer_benefits = {}
        self.epsilon = 5
        self.all_layers_assigned = False

    def get_server_price(self, request, context):
        return grpc_service_pb2.Price(price_value=self.price)
    
    def set_layers_assigned(self, request, context):
        self.all_layers_assigned = request.layers_assigned
        return grpc_service_pb2.ServerResponse(success=True)

    def bid_server(self, request, context):
        bid_value = request.bid_value
        if len(self.jk) < self.n_plus:
            self.profit[request.layer] = request.benefit - request.bid_value
            self.jk.append(request.layer)
            self.layer_benefits[request.layer] = request.benefit
            self.price = request.benefit - self.profit[request.layer]
            if len(self.jk) == self.n_plus:
                self.price = min(list(self.layer_benefits.values()) - list(self.profit.values()))
            return grpc_service_pb2.BiddingResult(server_id=self.server_id, 
                                                   Ack=True, 
                                                   price_value=self.price)
        
        elif request.bid_value >= self.price + self.epsilon:
            min_gain_layer_value = min(list(self.layer_benefits.values()) - list(self.profit.values()))
            min_gain_layer = list(self.profit.keys())[list(self.profit.values()).index(min_gain_layer_value)]
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
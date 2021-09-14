# Distributed_Deep_Learning_Inference
The Python implementation of distributed auction algorithm for multiple assignment (DAMA) of CNN inference.

Requirements:

- Torch 1.3.0
- Tensorflow-gpu 1.12.0

## Start Server:

``` python grpc_server.py 50051 ```

``` python grpc_server.py 50052 ```

## Start Client:

``` python grpc_client.py ```

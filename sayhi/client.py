__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-
import grpc
import sayhi_pb2
import sayhi_pb2_grpc


def run():
    # connect to grpc server
    channel = grpc.insecure_channel('127.0.0.1:5001')
    # sync call remote function and deal with the response.
    stub = sayhi_pb2_grpc.GreeterStub(channel)
    response = stub.SayHi(sayhi_pb2.HiRequest(name='grpc'))
    print(f"Greet client received:{response.message}")


if __name__ == '__main__':
    run()

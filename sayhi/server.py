__author__ = "vcancy"

# /usr/bin/python
# -*-coding:utf-8-*-
import time
from concurrent import futures
import sayhi_pb2
import sayhi_pb2_grpc
import grpc


class Demo(sayhi_pb2_grpc.GreeterServicer):
    """
    inherit the GreeterServicer and implement the function defined in proto file.
    """
    def SayHi(self, request, context):
        name = request.name
        return sayhi_pb2.HiReply(message=f"hi {name}")


def serve():
    """
    start a grpc server listening 5001 port
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sayhi_pb2_grpc.add_GreeterServicer_to_server(Demo(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    print('grpc server running...')
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

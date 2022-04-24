# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import types_pb2 as types__pb2


class GardensStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGarden = channel.unary_unary(
                '/Gardens/CreateGarden',
                request_serializer=types__pb2.CreateGardenRequest.SerializeToString,
                response_deserializer=types__pb2.CreateGardenResult.FromString,
                )
        self.GetGardens = channel.unary_stream(
                '/Gardens/GetGardens',
                request_serializer=types__pb2.GetGardensRequest.SerializeToString,
                response_deserializer=types__pb2.GetGardensResult.FromString,
                )


class GardensServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGarden(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGardens(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GardensServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGarden': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGarden,
                    request_deserializer=types__pb2.CreateGardenRequest.FromString,
                    response_serializer=types__pb2.CreateGardenResult.SerializeToString,
            ),
            'GetGardens': grpc.unary_stream_rpc_method_handler(
                    servicer.GetGardens,
                    request_deserializer=types__pb2.GetGardensRequest.FromString,
                    response_serializer=types__pb2.GetGardensResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Gardens', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gardens(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGarden(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Gardens/CreateGarden',
            types__pb2.CreateGardenRequest.SerializeToString,
            types__pb2.CreateGardenResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGardens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Gardens/GetGardens',
            types__pb2.GetGardensRequest.SerializeToString,
            types__pb2.GetGardensResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

import grpc.aio

from fastapi import Request


def get_garden_grpc_channel(request: Request) -> grpc.aio.Channel:
    return request.app.state.grpc_channel

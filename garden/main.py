import asyncio

from typing import Callable

import grpc

from fastapi import FastAPI

from garden_api import garden_pb2_grpc as garden_service
from grpc_service import GardenService

from db import get_conn


def _create_startup_handler(app: FastAPI) -> Callable:
    async def startup() -> None:
        app.state.db_conn = get_conn()

        server = grpc.aio.server()
        garden_service.add_GardensServicer_to_server(GardenService(app.state.db_conn), server)
        server.add_insecure_port('0.0.0.0:50051')

        await server.start()

        app.state.grpc_server = server
    
    return startup


def _create_shutdown_handler(app: FastAPI) -> Callable:
    async def shutdown() -> None:
        await app.state.grpc_server.stop(None)
        app.state.db_conn.close()
    
    return shutdown

def get_app() -> FastAPI:
    app = FastAPI()

    app.add_event_handler("startup", _create_startup_handler(app))
    app.add_event_handler("shutdown", _create_shutdown_handler(app))

    return app


app = get_app()

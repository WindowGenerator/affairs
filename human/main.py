import sys
import json

from typing import Callable

import grpc.aio

from fastapi import FastAPI, status

from routes import router as api_router


def _create_startup_handler(
    app: FastAPI,
) -> Callable:  # type: ignore
    async def startup() -> None:
        app.state.grpc_channel = grpc.aio.insecure_channel('{0}:{1}'.format('127.0.0.1', 50051))

    return startup


def _create_shudown_handler(app: FastAPI) -> Callable:  # type: ignore
    async def shutdown() -> None:
        await app.state.grpc_channel.close()

    return shutdown


def get_app() -> FastAPI:
    app = FastAPI()

    app.include_router(api_router)

    app.add_event_handler(
        "startup",
        _create_startup_handler(app),
    )
    app.add_event_handler(
        "shutdown",
        _create_shudown_handler(app),
    )

    return app

app = get_app()

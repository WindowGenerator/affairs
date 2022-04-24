from sqlite3 import Connection

import grpc

from garden_api import types_pb2 as garden_messages
from garden_api import garden_pb2_grpc as garden_service

from db import get_gardens, create_garden, ValidationError


class GardenService(garden_service.GardensServicer):
    def __init__(self, db_conn: Connection) -> None:
        self._db_conn = db_conn

    async def CreateGarden(self, request, context):
        metadata = dict(context.invocation_metadata())
        try:
            garden = create_garden(self._db_conn, name=request.name, place=request.place)
        except ValidationError as exc:
            context.set_details(str(exc))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

            garden = garden_messages.Garden()

        return garden_messages.CreateGardenResult(garden=garden)

    async def GetGardens(self, request, context):
        for garden in get_gardens(self._db_conn):
            yield garden_messages.GetGardensResult(garden=garden)

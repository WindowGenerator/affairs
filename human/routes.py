import json

import grpc

from typing import Optional
from fastapi import APIRouter, Depends, status, Request, Response
from grpc.aio import Channel
from google.protobuf.json_format import MessageToDict

from garden_api import garden_pb2_grpc as garden_service
from garden_api import types_pb2 as garden_messages

from dependencies import get_garden_grpc_channel
from schemas import CreateGardensInput


router = APIRouter()


@router.get("/ping/", status_code=status.HTTP_201_CREATED)
async def ping() -> None:
    return None


@router.get('/gardens/', status_code=status.HTTP_200_OK)
async def gardens_get(
    grpc_channel: Channel = Depends(get_garden_grpc_channel)
) -> Response:    
    garden = garden_service.GardensStub(grpc_channel)

    request = garden_messages.GetGardensRequest()
    
    async def get_gardens():
        response = garden.GetGardens(request)
        responses = list()

        async for r in response:
            responses.append(MessageToDict(r)["garden"])

        return responses

    return Response(json.dumps(await get_gardens()), headers={"Content-Type": "application/json"})


@router.post('/gardens/', status_code=status.HTTP_201_CREATED)
async def gardens_post(
    create_garden_args: CreateGardensInput, 
    grpc_channel: Channel = Depends(get_garden_grpc_channel)
) -> Response:
    garden = garden_service.GardensStub(grpc_channel)

    request = garden_messages.CreateGardenRequest(name=create_garden_args.name, place=create_garden_args.place)

    async def create_garden():
        response = garden.CreateGarden(request)
        
        try:
            return MessageToDict(await response)
        except grpc.RpcError as exc:
            status_code = exc.code()

            if grpc.StatusCode.INVALID_ARGUMENT != status_code:
                raise
            
            return {"error": exc.details()}

    
    return Response(json.dumps(await create_garden()), headers={"Content-Type": "application/json"})

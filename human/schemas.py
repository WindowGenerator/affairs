from pydantic import BaseModel


class CreateGardensInput(BaseModel):
    name: str
    place: str

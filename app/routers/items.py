
# from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class BaseItem(BaseModel):
    name: str
    description: str
    type: str


class InItem(BaseItem):
    id: int


class Car(InItem):
    type = "Car"
    year: int


class Plane(InItem):
    type = "Plane"


class CarOut(BaseItem):
    type = "Car"


class PlaneOUT(BaseItem):
    type = "Plane"


mycar = Car(name="my car", description="my lovely car", year=1980, id=1)
myplane = Plane(name="my plane", description="some plane", id=2)
data = {mycar.id: mycar, myplane.id: myplane}


# path params with PATH
# @router.get("/items/{id}", tags=["items"], response_model=Union[CarOut, PlaneOUT])
@router.get("/items/{id}", tags=["items"], response_model=BaseItem)
def get_item_by_path_id(id: int):
    print(data.get(id))
    return data.get(id, {"message": "item not found"})

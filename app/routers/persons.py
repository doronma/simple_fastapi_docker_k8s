from datetime import date
from enum import Enum
from typing import List

from app.ex import RestException
from fastapi import APIRouter, Body, HTTPException, Path, Query, status
from pydantic import BaseModel

router = APIRouter()


# Enumeration


class RequestType(str, Enum):
    Info = "info"
    Request = "request"


#  Pydantic models
class Person(BaseModel):
    id: int
    name: str
    joined: date


class Address(BaseModel):
    street_num: int
    street: str


dave = Person(id=1, name="Dave Doe", joined="2018-07-19")
gabi = Person(id=2, name="Gabi g", joined="2018-07-20")
data = {dave.id: dave, gabi.id: gabi}
datalist = list(data.values())


error_not_found = {"error": " user not found"}
post_ok = {"msg": "ok"}


# get all persons
@router.get("/persons", tags=["persons"], response_model=List[Person], response_description="The Person List",)
def get_persons():
    """
    # Get All Persons #  
    ## Using python documentation for swagger editor 
    Return: list of persons
    """
    return datalist


# path params
@router.get("/persons/{request_type}/{id}", tags=["persons"], response_model=Person)
def get_person_by_path(request_type: RequestType, id: int):
    print("selected request type: " + request_type.value)
    try:
        return data[id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found",
                            headers={"X-Error": "key error"})


# path params with PATH
@router.get("/persons/{id}", tags=["persons"], response_model=Person)
def get_person_by_path_id(id: int = Path(..., description="person id", gt=0, le=1000)):
    return data.get(id, error_not_found)


# Query params
@router.get("/persons_query", tags=["persons"])
def get_person_by_request(id: int,
                          request_type: RequestType = RequestType.Request,
                          status: str = None,
                          config: str = Query(...,
                                              regex="^[a-z]*$",
                                              title="configuration",
                                              description="some configuration",
                                              example="someconfig"
                                              ),
                          person_type: str = Query(None, alias="person-type"),
                          old: str = Query(None, deprecated=True),
                          category: str = Query(None, max_length=5, min_length=1)):

    print("selected request type: " + request_type.value)
    if category:
        print("selected category: " + category)
    if status:
        print("selected status: " + status)
    if person_type:
        print("selected person_type: " + person_type)
    print("selected config: " + config)
    return data.get(id, error_not_found)


# add person
@router.post("/persons", tags=["persons"], status_code=status.HTTP_201_CREATED)
def add_person(person: Person):
    data[person.id] = person
    return post_ok


# add person with query and path params
# {
#     "id": "3",
#     "name": "aviv",
#     "joined": "2018-07-21"
# }
@router.post("/persons/{name}", tags=["persons"], status_code=status.HTTP_201_CREATED)
def add_person_request(person: Person, name: str, check_name: bool = False):
    if not check_name or name == person.name:
        data[person.id] = person
        return post_ok
    else:
        raise RestException("person name mismatch")


# add preson multi params
# {
#     "person": {
#         "id": "3",
#         "name": "aviv",
#         "joined": "2018-07-21"
#     },
#     "address": {
#         "street_num": 5,
#         "street": "Hen"
#     },
#     "importance":8
# }
@router.post("/persons/extra/info", tags=["persons"], status_code=status.HTTP_201_CREATED)
def add_person_info(person: Person, address: Address, importance: int = Body(..., gt=0, lt=10)):
    print(person, address, importance)
    return post_ok

# add embeded object in body
# {
#     "person": {
#         "id": "3",
#         "name": "aviv",
#         "joined": "2018-07-21"
#     }
# }


@router.post("/persons/extra/embeded", tags=["persons"], status_code=status.HTTP_201_CREATED)
def add_person_embeded(person: Person = Body(..., embed=True)):
    print(person)
    return post_ok

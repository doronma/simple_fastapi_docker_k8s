from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()


class CustomerAddress(BaseModel):
    street_num: int
    street: str

    class Config:
        schema_extra = {
            "example": {
                "street": "Shoam",
                "street_num": 3
            }
        }


class Customer(BaseModel):
    id: int
    firstname: str = Field(None,
                           description="first name description",
                           title="Customer first name",
                           max_length=30,
                           example="Norma")
    lastname: str
    phone_numbers: List[str] = []
    address: CustomerAddress


post_ok = {"msg": "ok"}


# add customer
# {
#     "id": "3",
#     "firstname": "aviv",
#     "lastname": "2018-07-21",
#     "phone_numbers" : [
#         "123",
#         "456"
#     ],
#     "address":{
#         "street": "Shoam",
#         "street_num": 17
#     }
# }
@router.post("/customers", tags=["customers"], status_code=status.HTTP_201_CREATED)
def add_customer(customer: Customer):
    print(customer)
    return post_ok


# [
#     {
#         "id": "3",
#         "firstname": "aviv",
#         "lastname": "2018-07-21",
#         "phone_numbers": [
#             "123",
#             "456"
#         ],
#         "address": {
#             "street": "Shoam",
#             "street_num": 17
#         }
#     }
# ]
@router.post("/customer_list", tags=["customers"], status_code=status.HTTP_201_CREATED)
def add_customer_list(customer_list: List[Customer]):
    for customer in customer_list:
        print(customer)
    return post_ok

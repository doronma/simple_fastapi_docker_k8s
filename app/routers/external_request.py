
import os
import requests

from fastapi import APIRouter, Header, Request, status
from app.ex import RestException


router = APIRouter()


@router.get("/external_message", tags=["external_message"])
async def get_message(request: Request):
    #password = os.environ["SOME_PASSWORD"]
    try:
        EXPRESS_HOST = os.environ['EXPRESS_HOST']
        EXPRESS_POST = os.environ['EXPRESS_PORT']
    except KeyError as ex:
        return [{"error message ": "cannot find header: " + str(ex)}]
    request_headers = {}
    incoming_headers = ['x-request-id', 'x-b3-spanid',
                        'x-b3-parentspanid', 'x-b3-sampled', 'x-b3-flags', 'x-ot-span-context']

    for header in incoming_headers:
        try:
            request_headers[header] = request.headers[header]
        except KeyError as ex:
            print("cannot find header: " + str(ex))
    print(request_headers)
    response = requests.get('http://' + EXPRESS_HOST + ':' + EXPRESS_POST +
                            '/message', headers=request_headers)
    return [{"external message": response.json()}]

from typing import Dict

from fastapi import FastAPI, Header, Request, status
from fastapi.responses import JSONResponse


from app.ex import RestException
from app.routers import customers, items, persons, users, myredis, external_request


app = FastAPI()


@app.exception_handler(RestException)
async def person_exception_handler(request: Request, ex: RestException):
    return JSONResponse(
        status_code=401,
        content={"message": f"{ex.name} was thrown ..."},
    )


@app.get("/")
def read_root():
    return {"Hello": "World1"}


# Unchecked body
@app.post("/generaldata", status_code=status.HTTP_201_CREATED)
def get_general_data(data: Dict):
    print(data)
    return {"message": "ok"}


# header param
@app.get("/ping")
def ping(token: str = Header(...)):
    return {"message": "ping ok", "token": token}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["app_type"] = 'fastapi'
    return response

app.include_router(users.router)
app.include_router(persons.router)
app.include_router(customers.router)
app.include_router(items.router)
app.include_router(myredis.router)
app.include_router(external_request.router)

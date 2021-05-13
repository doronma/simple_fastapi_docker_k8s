FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip
RUN pip install redis
COPY ./app /app/app
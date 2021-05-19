FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip
RUN pip install redis
RUN pip install requests
COPY ./app /app/app
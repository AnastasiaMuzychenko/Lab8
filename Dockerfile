FROM python:3.11.4-slim-buster

RUN apt-get update && apt-get -y install libpq-dev gcc

WORKDIR /
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

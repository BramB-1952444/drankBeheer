# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /drankBeheer
COPY requirements.txt /drankBeheer/
RUN pip install -r requirements.txt
COPY . /drankBeheer/:WORKDIR
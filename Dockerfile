# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /drankBeheer
COPY requirements.txt /drankBeheer/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
COPY . /drankBeheer/:WORKDIR
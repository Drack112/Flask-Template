FROM python:3.8.0-alpine

WORKDIR /home/flask

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash

RUN pip install --upgrade pip
COPY ./requirements.txt /home/flask/requirements.txt

RUN pip install -r requirements.txt

COPY . /home/flask
EXPOSE 5000

RUN ls -la app/

ENTRYPOINT [ ".docker/entrypoint.sh" ]

FROM python:3.9-alpine
LABEL "https://offers.exigent-group.com"="Exigent Group"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY ./app /app

RUN adduser -D dev5

USER dev5


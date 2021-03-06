FROM python:3.9-alpine
LABEL "https://offers.exigent-group.com"="Exigent Group"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app

COPY ./app /app

RUN adduser -D dev5

USER dev5


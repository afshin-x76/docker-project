FROM python:3.8.3-alpine

RUN apk update \
    && apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk del build-deps

RUN pip3 install --upgrade pip

RUN pip3 install django pillow psycopg2-binary djangorestframework gunicorn celery redis 

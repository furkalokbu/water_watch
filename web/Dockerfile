FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /water_watch

WORKDIR /water_watch

COPY requirements.txt /water_watch/

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN apk --no-cache add \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev \
    ttf-dejavu \
    vim \
    binutils \
    gdal-dev \
    geos-dev

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apk del .tmp-build-deps

ADD . /water_watch/

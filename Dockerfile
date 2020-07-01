FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt
COPY ./lawpilots/ /app/lawpilots
WORKDIR /app/

RUN \
	apk update \
	&& apk add \
        --no-cache \
        --virtual build-dependencies \
        gcc \
        python3-dev \
        musl-dev \
    && apk add \
        --no-cache \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        fribidi-dev \
    && pip3 install -r requirements.txt \
    && apk del build-dependencies

CMD celery -A lawpilots worker -l INFO
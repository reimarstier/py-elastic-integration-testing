ARG LIB_RD_KAFKA_VERSION=1.0.0

FROM python:alpine3.7

RUN apk update && apk add build-base
RUN pip install pip-tools

WORKDIR /app
COPY ./ /app

RUN apk update && apk upgrade && apk add bash build-base sudo
RUN cd /tmp; wget http://github.com/edenhill/librdkafka/archive/${LIB_RD_KAFKA_VERSION}.tar.gz -O /tmp/librdkafka.tar.gz && \
  tar xf librdkafka.tar.gz --strip-components=1 && \
  ./configure --prefix /usr && make && make install

RUN pip-sync

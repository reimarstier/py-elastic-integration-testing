FROM python:alpine3.7
ARG LIB_RD_KAFKA_VERSION=1.0.0

RUN apk update && apk upgrade && apk add bash build-base sudo
RUN cd /tmp; wget https://github.com/edenhill/librdkafka/archive/v${LIB_RD_KAFKA_VERSION}.tar.gz -O /tmp/librdkafka.tar.gz && \
  tar xf librdkafka.tar.gz --strip-components=1 && \
  ./configure --prefix /usr && make && make install

WORKDIR /app
COPY ./ /app
RUN pip install pip-tools
RUN pip-sync
RUN pip install -U --pre pybuilder


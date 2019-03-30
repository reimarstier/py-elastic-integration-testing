#!/bin/sh

docker-compose -f docker-compose/testenv.yml up -d

docker-compose -f docker-compose/unittest.yml up

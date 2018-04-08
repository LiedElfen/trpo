#!/bin/sh

docker login -u "liedelfen" -p "$DOCKER_PASSWORD"
docker push liedelfen/trpo

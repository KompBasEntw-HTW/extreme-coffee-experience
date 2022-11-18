#!/bin/sh
cd products || exit 1
./mvnw install
cd .. || exit 1
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build
if [ "$1" = "products" ]; then
  cd products || exit 1
  ./mvnw quarkus:remote-dev
fi
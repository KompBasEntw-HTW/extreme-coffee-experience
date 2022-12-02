#!/bin/sh
# Build products service 
cd products || exit 1
./mvnw install

# Run docker compose
cd .. || exit 1
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build

# If products service is specified connect dev server to docker container
if [ "$1" = "products" ]; then
  cd products || exit 1
  ./mvnw quarkus:remote-dev
fi
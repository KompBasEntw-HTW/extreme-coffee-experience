#!/bin/sh
cd products
./mvnw quarkus:build
cd ..
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build

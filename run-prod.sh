#!/bin/sh
# Build products service 
cd products || exit 1
./gradlew build

# Run docker compose
cd .. || exit 1
docker compose -f docker-compose.yaml up -d --build


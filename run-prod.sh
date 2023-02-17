#!/bin/sh
# Build products service 
cd products || exit 1
./gradlew build
cd .. || exit 1

# Build basket service 
cd basket || exit 1
./gradlew build
cd .. || exit 1

# Build checkout service 
cd checkout || exit 1
./gradlew build
cd .. || exit 1

# Run docker compose
docker compose --env-file ./.env -f docker-compose.yaml up -d --build


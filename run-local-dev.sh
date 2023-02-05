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
docker compose --env-file ./.env.local -f docker-compose.yaml -f docker-compose.dev.yaml up -d --build

# If products service is specified connect dev server to docker container
if [ "$1" = "products" ]; then
  cd products || exit 1
  ./gradlew quarkusRemoteDev
fi

# If basket service is specified connect dev server to docker container
if [ "$1" = "basket" ]; then
  cd basket || exit 1
  ./gradlew quarkusRemoteDev
fi

# If basket service is specified connect dev server to docker container
if [ "$1" = "checkout" ]; then
  cd checkout || exit 1
  ./gradlew quarkusRemoteDev
fi

# extreme-coffee-experience
Deployment/development repo Extreme Coffee Experience.  
Includes all microservices as submodules and the the deployment files.  

To start up application in production mode run:  
```console
docker compose -f docker-compose.yaml up --build -d
```

Services will build and run but hot module reloading is not possible.  

To develop application locally with all services running and hot module reloading enabled run:  
```console
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d
```

If you add any new dependencies you need to add the `--build` flag.

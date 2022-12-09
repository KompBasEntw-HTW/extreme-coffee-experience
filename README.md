# extreme-coffee-experience
Deployment/development repo Extreme Coffee Experience.  
Includes all microservices as submodules and the the deployment files.  

To pull this repository including all submodules you need to run:

```console
git clone --recurse-submodules git@github.com:KompBasEntw-HTW/extreme-coffee-experience.git
```

~~To get changes in all submodules in future pulls from main repo run:~~ 
```diff
- git config --global submodule.recurse true
```

My bad please turn this off again with
```console
git config --global submodule.recurse false
```

Switch all submodules to main branch
```console
git submodule foreach git switch main
```

To update all submodule to latest commit on branch run 
```console
git submodule foreach git pull
```

To be ablo to commit you need to first install commitlint in this repo. Just run:
```console
npm install
```

Submodules are their own repositories. They have their own commit history and everything. You can therefore use your own git workflow inside of them.
To reflect the changes done in a submodule you have to commit them to this repository, so this repo when updated from somewhere else, points to the desired version of the submodule. You can always do it after closing a pull request or implenting a feature. 

There is a simple shell script called `run-local-dev.sh` to startup the application in development mode.
Just run:
```console
./run-local-dev.sh
```

If you want to connect your backend microservice dev server to the docker container just specify which service you want to have hot reloading on e.g:
```console
./run-local-dev.sh products
```


<!---
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


-->

## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/fastapi)

### PHP/Laravel application

Project structure:
```
├── 10
    ├── Dockerfile
├── 10-arm
    ├── Dockerfile
├── Project
    ├── entrypoint
        ├── laravel_entrypoint.sh
        ├── nginx_entrypoint.sh
    ├── nginx
        ├── default.conf
    ├── src
    ├── docker-compose.yaml

```

[_compose.yaml_](compose.yaml)
```
services:
  db
  app
  nginx (optional)

```

## Deploy with docker compose

```shell
DB_USER="user" DB_PASSWORD="password" ROOT_PASSWORD="root" docker compose up -d --build
```
## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS                                               NAMES
4920d6ea85d8   nginx:latest              "/usr/local/bin/entr…"   8 days ago          Up About an hour             0.0.0.0:81->80/tcp, :::81->80/tcp                                                                                     el_archivador-nginx
55e64bbfa991   ikerlorente/laravel:v10   "/usr/local/bin/entr…"   2 weeks ago         Up About an hour             0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                                                             el_archivador-app
7a1b036573a7   mysql                     "docker-entrypoint.s…"   2 weeks ago         Up About an hour (healthy)   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                                                  el_archivador-db

```

After the application starts, navigate to `http://localhost:8000` in your web browser and you should see the app running

Stop and remove the containers
```
$ docker compose down
```

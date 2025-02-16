# Project: FastAPI/Flask

## Description
Este proyecto es una aplicación web desarrollada utilizando **Flask-Migrate** (para el manejo de migraciones) y **FastAPI** (para el desarrollo de APIs). El objetivo de esta aplicación es proporcionar una solución robusta para manejar datos y servicios REST.

## Estructura del Proyecto
```
FastApi_Flask/
├── Dockerfile
├── README.md
├── api
│   ├── controllers
│   │   ├── UserController.py
│   ├── database.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── __pycache__
│   │   │   └── env.cpython-39.pyc
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 6b836cb6b8f7_initial_migration.py
│   ├── models
│   │   ├── User.py
│   └── wait-for-db.sh
├── docker-compose.yml
└── requirements.txt
```

## Estructura de case de datos
1. Usuarios

   ```
   Usuarios
        firstName: string(50)
        lastName: string(50)
   ```

## Requisitos previos
- Tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) en su máquina local.

## Uso
1. Clone el repositorio en su máquina local:

   ```
   git clone <URL>
   ```

2. Navegar hasta la carpeta del proyecto creada y despliega el contenedor:

   ```
   cd FastApi_Flask
   docker-compose up -d
   ```

3. Abrir un navegador web y acceder a la aplicación en la dirección `http://localhost:8000/docs`.
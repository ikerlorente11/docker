### CREAR IMAGEN A PARTIR DE UN DOCKERFILE
~~~
docker build -t "imagename:tag" .
~~~

### CREAR NETWORK
~~~
docker network create "network name"
~~~

### CREAR CONTENEDOR
~~~
docker run -t -d -p "hostport":"dockerport" --name "nombre" --net="network" -v "hostdir":"dockerdir" "imagename"
~~~
# Clusters con Apache Hadoop 
Código para las prácticas de la asignatura de "Gestión y Almacenamiento de Datos Masivos" - Máster MADM

- A1. Apache Hadoop sobre un nodo
  - MapReduce
  - HDFS
  - PIG
  - SQOOP
- A2. Apache Ambari 
- A3. Cloudera sobre docker
  - HUE
  - IMPALA
  - HIVE
- A4. Apache SPARK
   - Scala
- A5. Cluster de Apache Spark
- A6. Apache Zeppelin



# Actividades del entorno Hadoop con dockers

## PIG


```
docker pull hakanserce/apache-pig
```

Sin acceso a puertos de hadoop:
```
docker run -i -t --name=mypig hakanserce/apache-pig /etc/bootstrap.sh -bash
```

O con opción a hadoop web ui interface (listado de puertos: https://blog.cloudera.com/blog/2009/08/hadoop-default-ports-quick-reference/):

```
docker run -i -t --name=mypig -p 50070:50070 hakanserce/apache-pig /etc/bootstrap.sh -bash  <! Vinculemos puertos !>
```

Ya podemos lanzar programas con pig:
```
pig
```



## Hadoop

Hadoop ya viene instalado con la imagen anterior (pero esta imagen nos permitirá montar un cluster)
https://github.com/sequenceiq/hadoop-docker

```
docker pull sequenceiq/hadoop-docker:2.7.1
docker run --name=myhadoop -it  sequenceiq/hadoop-docker:2.7.1  /etc/bootstrap.sh -bash
```

## SPARK

Desde el proyecto BBVADATA, han creado está interesante imagen, con un notebook de jupiter para crear aplicaciones de SPARK con PySPARK
https://github.com/bbvadata/docker-blog-example

O una versión más cruda en:
https://hub.docker.com/r/sequenceiq/spark/


## Curiosidades
Como crear un cluster hadoop con varios containers
https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f


### DOCKER COMMANDS

Detach:
```
Ctrl+p y Ctrl+q 
```

Attach:
```
docker attach <container>
```

Ver en ejecución
```
docker ps 
```

Ver containers:
```
docker ps -a
```

Ver un container en detalle:
```
docker inspect <container>
```

¿Cómo compartir una carpeta?
```
 -v ~/hola:/home/user/adios
 ```

¿Cómo asignarles un nombre?
```
--name=mypig 
```

#### Varios
```
docker container ls
docker container stop <container>
docker container ls -a
docker container rm <container>
docker image ls
docker image rm <image>
docker exec -it <container name> /bin/bash
```

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

## PIG


```
docker pull hakanserce/apache-pig
```
docker run -i -t --name=mypig hakanserce/apache-pig /etc/bootstrap.sh -bash
docker run -i -t --name=mypig -p 50070:50070 hakanserce/apache-pig /etc/bootstrap.sh -bash  <! Vinculemos puertos !>

pig

(ports: https://blog.cloudera.com/blog/2009/08/hadoop-default-ports-quick-reference/)


## Hadoop

https://github.com/sequenceiq/hadoop-docker

docker pull sequenceiq/hadoop-docker:2.7.1
docker run --name=myhadoop -it  sequenceiq/hadoop-docker:2.7.1  /etc/bootstrap.sh -bash


SPARK
-----

1 https://github.com/bbvadata/docker-blog-example
2 https://hub.docker.com/r/sequenceiq/spark/


A composition of Cluster hadoop:
https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f


DOCKER COMMANDS
---------------

Detach:
Ctrl+p y Ctrl+q 

Attach:
docker attach <container>

Ver en ejecución
docker ps 

Ver containers:
docker ps -a

Ver un container en detalle:
docker inspect <container>

¿Cómo compartir una carpeta?
 -v ~/hola:/home/user/adios

¿Cómo asignarles un nombre?
--name=mypig 

Varios:
docker container ls
docker container stop <container>
docker container ls -a
docker container rm <container>
docker image ls
docker image rm <image>

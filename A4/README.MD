#Instalación de APACHE SPARK con SCALA (standlone)

testeado sobre:
- Centos7 (4gB)
- Scala 2.12.1
- Spark 2.1
- Hadoop 2.7

##Preparación
yum install wget

##Instalación de Java
yum install java-1.8.0-openjdk*


##Instalación de Scala
wget http://www.scala-lang.org/files/archive/scala-2.12.1.tgz

tar xvf scala-2.12.1.tgz

sudo mv scala-2.12.1 /usr/lib

sudo ln -s /usr/lib/scala-2.12.1 /usr/lib/scala



##Descarga de SPARK: http://spark.apache.org/downloads.html
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz

tar xf spark-2.1.0-bin-hadoop2.7.tgz

mkdir /usr/local/spark

cp -r spark-2.1.0-bin-hadoop2.7/* /usr/local/spark

##En sources: ~/.bashrc
export PATH=$PATH:/usr/lib/scala/bin

PATH=$PATH:$HOME/bin:/usr/local/spark/bin

source ~/.bashrc

##Running spark:
spark-shell

```
http://<host>:4040
```
##Ejemplo:
```
val data = 1 to 1000000000
sc.parallelize(data).sum()
```

##Actividad:
Utilizando el primer cluster (A1) realizamos nuestro contar frecuencia de palabras: http://spark.apache.org/

```
text_file = spark.textFile("hdfs://...")
 
text_file.flatMap(lambda line: line.split())
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a+b)
```
   
# O con python
Tener configurado python en Centos: 
```
yum -y install epel-release
yum install python-pip python-wheel
pip install pandas
```
pyspark


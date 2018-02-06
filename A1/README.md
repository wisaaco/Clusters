# Instalación de Apache Hadoop en un nodo

Testeado sobre:
- Ubuntu Server 14.02 / 16.04
- Apache Hadoop 2.7.3 / 3.0.0

# 1 Instalación de Java: JDK free o JDF de Oracle
## 1.a
```
sudo apt-get install default-jdk
java -version 
```

## 1.b Instalación de JDK de Oracle (yo he usado está opción)
 ```
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
 ```
# 2. Configuración de usuario y grupo para acceder a los servicios del cluster de Hadoop (opcional)
# Atención: está opción compromete el resto de comandos (pensad sobre que usuario estáis aplicando los futuros comandos)
```
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
```

# 3. Todos los procesos de Hadoop realizan comunicaciones via SSH. Ésta ha de habilitarse para que no haya credenciales (password: SSH sin credenciales)
```
su hduser 

ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
## Modificar el fichero de configuracion de SSH: con la siguiente linea de 'yes'
```
sudo vi /etc/ssh/sshd_config
PasswordAuthentication yes
```
## Se reinicia el servicio
```
sudo service ssh restart
```
## Se comprueba que el servicio no solicita el password a la segunda vez de conectarse via ssh
```
ssh localhost
exit
```
 

# 3.B Esta opción ha de realizarse sobre instancias de AWS: 

## Se ha de modificar el fichero de /etc/hosts para identificar el hostname de la instancia de AWS como localhost. Para ello se añade el hostname (ip-XX-XX-XX-XX) a la IP: 127.0.0.1 tal como podéis ver aquí:
```
vi /etc/hosts
127.0.0.1 localhost ip-172-30-0-124
```

# 4. Descarga y Deployment de Hadoop

## Tenéis que acceder http://hadoop.apache.org/releases.html y buscar el binary de la última versión (3.0.0). Copiar el link e introducirlo en el comando wget
```
wget <<link.tar.gz>>
tar xvzf  hadoop-x.... tar.gz
sudo mv * /usr/local/hadoop (ojo)
sudo chown -R hduser:hadoop /usr/local/hadoop
sudo mkdir -p /app/hadoop/tmp (*)
sudo chown hduser:hadoop /app/hadoop/tmp (*)
```

# 5. Configuración de las variables de entorno

## ¿Dónde esta JAVA?
```
readlink -f `which java`

export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```

## Escribimos las variables del usuario (pensad en las diferentes paths)
vi ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export HADOOP_HOME=/home/ubuntu/hadoop-XXXXXX
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```
## Cargamos las variables
```
source ~/.bashrc
```

## 5. B Configuración de archivos de Hadoop. Actualizar el contenidod e los diferentes ficheros de hadoop.

### File: /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```

### File:/usr/local/hadoop/etc/hadoop/hdfs-site.xml

### ¿Para que sirven estos directorios?
```
sudo mkdir -p /usr/local/hadoop_store/hdfs/namenode
sudo mkdir -p /usr/local/hadoop_store/hdfs/datanode
sudo chown -R hduser:hadoop /usr/local/hadoop_store
```

```
 <property>
  <name>dfs.replication</name>
  <value>1</value>
 </property>
 <property>
   <name>dfs.namenode.name.dir</name>
   <value>file:/usr/local/hadoop_store/hdfs/namenode</value>
 </property>
 <property>
   <name>dfs.datanode.data.dir</name>
   <value>file:/usr/local/hadoop_store/hdfs/datanode</value>
 </property>
```

### File:/usr/local/hadoop/etc/hadoop/core-site.xml
```
 <property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description></description>
 </property>
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://localhost:9000</value>
  <description></description>
 </property>
```

### File:/usr/local/hadoop/etc/hadoop/mapred-site.xml
 ```
  <property>
  <name>mapred.job.tracker</name>
  <value>localhost:9001</value>
  <description></description>
 </property>
 ```
 
### File:/usr/local/hadoop/etc/hadoop/yarn-site.xml
 ```
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
 ```
 
# 6. Creación del sistema de ficheros HDFS
```
hadoop namenode -format
```

# 7. Arrancar scripts de Hadoop (HDFS y YARN)

/usr/local/hadoop/sbin/start-dfs.sh

/usr/local/hadoop/sbin/start-yarn.sh

or: 

start-dfs.sh

start-yarn.sh

### ¿Os funciona?
```
jps
```

#### Está debera de ser la salida:
```
5744 ResourceManager
5876 NodeManager
5158 NameNode
5290 DataNode
6445 Jps
5485 SecondaryNameNode
```
# END

```
hdfs dfs -ls /
hdfs dfs -mkdir /input
```
http://<host>:50070

```
#TODO:
- Configuración de Yarn: http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-common/SingleCluster.html#YARN_on_Single_Node

```
http://<host>:8088
```

#Instalación de Apache Hadoop en un nodo

Testeado sobre:
- Ubuntu Server 14.02
- Apache Hadoop 2.7.3

##Instalación de Java
sudo apt-get install default-jdk
java -version 

##Configuración de usuario

sudo addgroup hadoop

sudo adduser --ingroup hadoop hduser

sudo adduser hduser sudo


##Habilitar SSH sin credenciales
su hduser

ssh-keygen -t rsa -P ""

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

works?

##Deployment de Hadoop
wget … <<http://hadoop.apache.org/releases.html>>

tar xvzf  hadoop-2…. tar.gz

sudo mv * /usr/local/hadoop

sudo chown -R hduser:hadoop /usr/local/hadoop

sudo mkdir -p /app/hadoop/tmp

sudo chown hduser:hadoop /app/hadoop/tmp


##Variables de entorno
vi ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export HADOOP_INSTALL=/usr/local/hadoop
export PATH=$PATH:$HADOOP_INSTALL/bin
export PATH=$PATH:$HADOOP_INSTALL/sbin
export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_HOME=$HADOOP_INSTALL
export HADOOP_HDFS_HOME=$HADOOP_INSTALL
export YARN_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_INSTALL/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_COMMON_LIB_NATIVE_DIR"
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true"
```
source ~/.bashrc

##Configuración de archivos de Hadoop
###File: /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
```

###File:/usr/local/hadoop/etc/hadoop/hdfs-site.xml
sudo mkdir -p /usr/local/hadoop_store/hdfs/namenode

sudo mkdir -p /usr/local/hadoop_store/hdfs/datanode

sudo chown -R hduser:hadoop /usr/local/hadoop_store

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

###File:/usr/local/hadoop/etc/hadoop/core-site.xml
```
 <property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description></description>
 </property>
<property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description></description>
 </property>
```

###File:/usr/local/hadoop/etc/hadoop/mapred-site.xml
 ```
  <property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description></description>
 </property>
 ```
##Creación del sistema de ficheros HDFS

hadoop namenode -format

##Arrancar scripts
/usr/local/hadoop/sbin/start-dfs.sh

/usr/local/hadoop/sbin/start-yarn.sh

##Funciona?
jps
```
http://<host>:50070
```
#TODO:
- Configuración de Yarn: http://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-common/SingleCluster.html#YARN_on_Single_Node
```http://<host>:8088```

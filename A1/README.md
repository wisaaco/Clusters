#Instalación de Apache Hadoop en un nodo

Testeado sobre:
- Ubuntu Server 14.02
- Apache Hadoop 2.7.3

##Instalación de Java
```
sudo apt-get install default-jdk
java -version 
```

#or (yo he usado está)
 ```
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
 ```
##Configuración de usuario (opcional)
```
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
```

##Habilitar SSH sin credenciales
```
su hduser (si anterior)

ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
#Modificar fichero configuracion:  
```
sudo vi /etc/ssh/sshd_config
PasswordAuthentication yes

sudo service ssh restart

ssh localhost

exit
 
```

# AWS: 

```
$ cat /etc/hosts
127.0.0.1 localhost ip-172-30-0-124
```

##Deployment de Hadoop
```
wget … <<http://hadoop.apache.org/releases.html>>
tar xvzf  hadoop-x.X... tar.gz
sudo mv * /usr/local/hadoop (ojo)
sudo chown -R hduser:hadoop /usr/local/hadoop
sudo mkdir -p /app/hadoop/tmp (*)
sudo chown hduser:hadoop /app/hadoop/tmp (*)
```

##Variables de entorno

# Donde esta JAVA?
```
readlink -f `which java`

export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```

vi ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export HADOOP_HOME=/home/ubuntu/hadoop-XXXXXXXXXX
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

```
source ~/.bashrc

##Configuración de archivos de Hadoop
###File: /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
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
  <name>fs.defaultFS</name>
  <value>hdfs://localhost:9000</value>
  <description></description>
 </property>
```

###File:/usr/local/hadoop/etc/hadoop/mapred-site.xml
 ```
  <property>
  <name>mapred.job.tracker</name>
  <value>localhost:9001</value>
  <description></description>
 </property>
 ```
 
###File:/usr/local/hadoop/etc/hadoop/yarn-site.xml
 ```
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
 ```
 
##Creación del sistema de ficheros HDFS

hadoop namenode -format

##Arrancar scripts
/usr/local/hadoop/sbin/start-dfs.sh

/usr/local/hadoop/sbin/start-yarn.sh

or: 

start-dfs.sh

start-yarn.sh

##Funciona?
jps

```
5744 ResourceManager
5876 NodeManager
5158 NameNode
5290 DataNode
6445 Jps
5485 SecondaryNameNode
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

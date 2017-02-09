#Configuración de un cluster mediante Apache Ambari 

testeado sobre:
- Ubuntu Server 14.02
- Apache Ambari 2.2.2

#Activación user root en SSH config
#Instalación de NTP
sudo apt-get update

sudo apt-get dist-upgrade

sudo apt-get install ntp

#Definir HOSTNAMEs en todos los nodos
/etc/hosts


#Configuración SSH password less
ssh-keygen -t rsa -P ""

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

##En resto de nodos: 
ssh-copy-id root@[hosts]

#Desabilitar Transparent Huge Pages (THP):
echo never >/sys/kernel/mm/transparent_hugepage/enabled

cat /sys/kernel/mm/transparent_hugepage/enabled

always madvise [never] ???

#Descarga de Ambari en nodo HOST
cd /etc/apt/sources.list.d

wget http://public-repo-1.hortonworks.com/ambari/ubuntu12/2.x/updates/2.2.2.0/ambari.list

apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD

apt-get update

apt-get install ambari-server

ambari-server setup

ambari-server start
```
http://<ambari-server-host>:8080
```


#Instalación de Cloudera sobre Docker

requisitos:
- Centos7
- Docker instalado
- Image: cloudera/quickstart:latest Descargada (~4GB): docker pull cloudera/quickstart:latest

#Pre-bugs:
Desactivar el firewall y activar el servicio docker

service firewalld stop

service docker start

#Run Cloudera:
docker run - -hostname=quickstart.cloudera - -privileged=true -t -i -p 8888:8888 -p 80:80 cloudera/quickstart /usr/bin/docker-quickstart

```
http://<cloudera.host>/
```

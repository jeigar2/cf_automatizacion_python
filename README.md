# cf_automatizacion_python
Clase Automatización con Python - Bootcamp de DevOps, Nivel 2
# Clase - Automatización con Python Bootcamp de DevOps, Nivel 2

- Requerimientos instalar `multipass` (para tener entornos remotos)
- libreria [python-dotenv](https://pypi.org/project/python-dotenv/)

## multipass

- Pasos
  - instalar
  - crear entorno
  - listar entornos
  - conectar entorno
  - permitir conexion ssh

### instalar

```sh
sudo snap install multipass
```

- comprobar version

```sh
multipass --version
```

- salida

```log
multipass   1.15.0
multipassd  1.15.0
```

## crear entorno

```sh
multipass find
```

- salida

```log
Image                       Aliases           Version          Description
core                        core16            20200818         Ubuntu Core 16
core18                                        20211124         Ubuntu Core 18
core20                                        20230119         Ubuntu Core 20
core22                                        20230717         Ubuntu Core 22
core24                                        20240603         Ubuntu Core 24
20.04                       focal             20250218.1       Ubuntu 20.04 LTS
22.04                       jammy             20250221         Ubuntu 22.04 LTS
24.04                       noble,lts         20250221         Ubuntu 24.04 LTS
24.10                       oracular          20250129         Ubuntu 24.10
daily:25.04                 plucky,devel      20250128         Ubuntu 25.04
appliance:adguard-home                        20200812         Ubuntu AdGuard Home Appliance
appliance:mosquitto                           20200812         Ubuntu Mosquitto Appliance
appliance:nextcloud                           20200812         Ubuntu Nextcloud Appliance
appliance:openhab                             20200812         Ubuntu openHAB Home Appliance
appliance:plexmediaserver                     20200812         Ubuntu Plex Media Server Appliance

Blueprint                   Aliases           Version          Description
anbox-cloud-appliance                         latest           Anbox Cloud Appliance
charm-dev                                     latest           A development and testing environment for charmers
docker                                        0.4              A Docker environment with Portainer and related tools
jellyfin                                      latest           Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media.
minikube                                      latest           minikube is local Kubernetes
ros2-humble                                   0.1              A development and testing environment for ROS 2 Humble.
ros2-jazzy                                    0.1              A development and testing environment for ROS 2 Jazzy.
```

- instalar la version `core20` - 20230119 - Ubuntu Core 20

```sh
multipass launch core20
```

### listar entornos

```sh
multipass ls
```

- salida

```sh
Name                    State             IPv4             Image
fruitful-stag           Running           10.174.77.28     Ubuntu Core 20
```

### conectar entorno

```sh
multipass shell fruitful-stag 
```

- salida

```log
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-202-generic x86_64)
 * Ubuntu Core:     https://www.ubuntu.com/core
 * Community:       https://forum.snapcraft.io
 * Snaps:           https://snapcraft.io

This Ubuntu Core 20 machine is a tiny, transactional edition of Ubuntu,
designed for appliances, firmware and fixed-function VMs.

If all the software you care about is available as snaps, you are in
the right place. If not, you will be more comfortable with classic
deb-based Ubuntu Server or Desktop, where you can mix snaps with
traditional debs. It's a brave new world here in Ubuntu Core!

Please see 'snap --help' for app installation and updates.
Last login: Sun Feb 23 02:24:55 2025 from 10.174.77.1
ubuntu@fruitful-stag:~$ 
```

## permitir conexion ssh 

- en la máquina local, se agrega la máquina remota `10.174.77.28`

```sh
ssh-keyscan -t ed25519 10.174.77.28 >> ~/.ssh/known_hosts
```

- clave publica [url](https://www.ispmalaga.es/ssh-con-clave-publica/)

- copio en remoto el fichero de clave publica con extension `.pub`

```sh
scp /home/igg/.ssh/id_rsa.pub ubuntu@10.174.77.28:/home/ubuntu
```

- me conecto a la máquina remota
  - hago una copia de seguridad del fichero `~/.ssh/authorized_keys`
  - agrego el contenido de la clave pública
  - borro el fichero copiado remotamente `/home/user/id_rsa.pub`

```sh
multipass shell fruitful-stag 

cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys_bck
echo `cat ~/id_rsa.pub` >> ~/.ssh/authorized_keys
rm /home/user/id_rsa.pub
```

## ejecutar proyecto

- obtener las dependencias

```sh
pip install -r requirements.txt
```

## Jinja2

- Se utiliza para templates donde se puede definir variables con {{ variable }}
- Que se resuelven en tiempo de ejecución
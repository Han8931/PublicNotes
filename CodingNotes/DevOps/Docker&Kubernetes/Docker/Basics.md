---
tags:linux, docker, kubernetes 
---

# What is Docker?

- Docker is a tool for running applications in an _isolated environment_. 
	- They have their own processes, network but _share the same OS kernel_
- It is similar to virtual machine
	- However, VM has its own OS kernel
- Standard for software development
- The _docker host_ is the base traditional OS server where the OS and processes are running in normal (non-container) mode. So the OS and processes you start by actually powering on and booting a server (or VM) are the docker host. The processes that start within containers via docker commands are your containers.

## Containers vs VM
- Containers are an _abstraction_ at the app layer that packages _code_ and _dependencies_ together. 
	- Run quickly
- Virtual machines are an abstraction of physical hardware turning one server into many servers. Each VM includes a full copy of an operating system, the application, necessary binaries and libraries. 

## Containers vs Image 
### Image
- Image is a _template_ for creating an environment of your choice
- snapshot

### Containers 
- _Running instance of an image_
	- You can run image from container

# Installation 

1. `sudo pacman -S docker` : for Arch users
2. `docker --version`
3. `sudo systemctl start docker`: start the docker daemon manually
	- We need to run this command manually for arch linux. 
4. `docker run hello-world` : test your Docker installation

## Run Docker Command without `sudo`

```bash
sudo groupadd docker # Create a group
sudo usermod -aG docker sally # Add an user `sally` to `docker` group
su - sally # Switch user
```

To check users in _docker_ group:
- `grep /etc/group -e "docker"`

As you created a new group the system needs to re-evaluate the group membership.

You may run any of the following methods.

Log out from the current terminal and log back in. You may also run `exec su -l $USER` or `newgrp docker` command.

If you are comfortable you can restart the docker service as well.

```
sudo systemctl restart docker
```


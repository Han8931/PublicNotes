---
tags:linux,docker,kubernetes 
---

# What is Docker?
>- Docker is a tool for running applications in an isolated environment. 
>- It is similar to virtual machine
>- Standard for software development

## Containers vs VM
- Containers are an _abstraction_ at the app layer that packages _code_ and _dependencies_ together. 
	- Run quickly
- Virtual machines are an abstraction of physical hardware turning one server into many servers. Each VM includes a full copy of an operating system, the application, necessary binaries and libraries. 

## Image & Containers
### Image
- Image is a template for creating an environment of your choice
- snapshot

### Containers 
- Running instance of an image
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


# Tutorial 

- `docker pull <images>`: e.g., `docker pull nginx`
- `docker images` : list images I have
	- show: nginx:latest image
 
## Basic Commands

### Check Status
- `docker ps` 
	- List running containers
- `docker ps -al`
	- Show all info
- `docker ps --format=ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n`
	- Allows to make it more readable
	- We can keep this info by
		- `export FORMAT=ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n`
		- `docker ps --format=$FORMAT`

### Run & Stop Container
- `docker run nginx:latest` : latest is the tag. Without the tag, it will download the lastest version as default. 
	- This runs a container, then just open a new termianl and run:
	- `docker container ls` : show conatiners
	- Quit the container by simply `CTRL+C`
- `docker run -d nginx:latest` : run the container in the attached mode. 
- `docker run -d -p 8080:80 nginx:latest`
	- In my browser: `localhost: 8080` or `http://localhost:8080/dist/index.html`
- `docker run -d -p 8080:80 -p 3030:80 nginx:latest`
	- We can map more than one port

### Stop and Resume Container
- `docker stop <CONTAINER ID>` : stop container
	- In case you can still see the container in your browser by localhost, check the cache setting in your browser.
	- List all numeric container ids:
		- `docker ps -aq`
- Note that we just stopped it, but haven't removed it, so we can resume it. 
	- `docker start <CONTAINERID/NAMES>`
 
### Delete Container
- How do we delete containers?
	- To delete a single container 
		- `docker rm <CONTAINERID/NAMES>`
	- To delete all containers:
		- `docker rm $(docker ps -aq)`
		- Note that we cannot remove running containers
			- `docker rm -f $(docker ps -aq)` : force removing even running containers
	- Check with `docker ps -a`
- Note that if you create an image with an existing name and tag, it would show `<none>` image repository. This kinda image is often called _dangling image_.
	- To delete such repos: 
		- `docker system prune`
		- `docker image prune` : delete only dangling images
 
### Naming Containers
- `docker run --name <NAME> -d -p 8080:80 nginx:latest`

### Volumes
Allows us to share data (Files and Dir). 
- Between host and container 
- Between containers 

#### Host and Container
- `docker run --name website -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 nginx:latest`
	- By running this command, the container can bring files inside the `PWD`.
	- `website` is my container's name 
	- `-v` : create a volume named by `PWD`
	- The files will be stored at `/usr/share/nginx/html`
- To get files from the container 
	- `docker exec -it <dockername> bash`: this command activate bash command. 
	- We can use bash commands freely e.g., `ls`.
	- However, we cannot write something inside `html` directory in container, since it is the `readonly` directory. To resolve this issue, we have to run it without `ro` argument. 
		- `docker run --name website -v $(pwd):/usr/share/nginx/html -d -p 8080:80 nginx:latest`

#### Between Containers
- `docker run --name website-copy --volumes-from website -d -p 8081:80 nginx`
	- It creates a connection between `website-copy` and `website`

### Dockerfile
- Build own images by creating _dockerfile_

#### Create Dockerfile
Inside the directory, create a file named `Dockerfile` with the following commands
```
FROM nginx:latest
ADD . /usr/share/nginx/html # add all files to <dest>
```

```
FROM node:latest
WORKDIR /app
ADD . .
RUN npm install 
CMD node index.js
```

- Docker runs instructions in a `Dockerfile` in order. 
- Dockerfile must begin with a `FROM` instruction. 
	- It specifies the parent image from which you are building. 
- You can write a comment with `#`
- `WORKDIR` : Sets the working directory for the instructions that follow
- `ADD` : Copy files and directories to the container. 
	- `ADD . .` : add all contents to `/app`
- `RUN echo hello` : we are running some commands
	- Runs a Linux command


#### Docker Build
- Create an _image_ from the _Dockerfiile_
	- `docker build --tag website:latest .`  : docker file is inside, so just use `.`
		- `--tag` or `-t`
		- `docker image ls` : check 
		- `website`: name / `latest`: tag
- Now we don't have to create a volume. Simply run
	- `docker run --name website -d -p 8080:80 website:latest`
	- You can check by using your browser

#### Ignore Files 
- Create `.dockerignore` : similar to `.gitignore`
	- `.git`
	- `Dockerfile`
	- `*.gulp.js`
	- `node_modules`
	- `dir/**`

### Caching and Layers
Say that you are updating user information in `index.js`, then you have to build a new image and run a container.  We shouldn't waste time for simply updating some information. To avoid this, we can leverage caching.  A simple trick is to add caching file before adding all files.
```
FROM node:latest
WORKDIR /app
ADD package*.json ./
RUN npm install 
ADD . .
CMD node index.js
```

### [Alpine](https://hub.docker.com/_/alpine) for Minimal Image

> [Alpine Linux](https://alpinelinux.org/) is a Linux distribution built around [musl libc](https://www.musl-libc.org/) and [BusyBox](https://www.busybox.net/). The image is only 5 MB in size and has access to a [package repository](https://pkgs.alpinelinux.org/) that is much more complete than other BusyBox based images. This makes Alpine Linux a great image base for utilities and even production applications. [Read more about Alpine Linux here](https://alpinelinux.org/about/) and you can see how their mantra fits in right at home with Docker images.

When you pull or create standard docker images, their size is quite huge.  

#### Pulling Alpine Images
- `docker pull node:alpine` : Alpine version of node
	- `docker image ls` : to check its size... it is significantly smaller than the standard node docker image `node:latest`.
- `docker pull nginx:alpine`

### Tags and Versions





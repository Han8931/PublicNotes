# Introduction
A Docker image is a read-only template that describes how to create a Docker container. The image is the instructions while the container is the actual running instance of an image. To continue our apartment analogy from earlier in the chapter, an image is the blueprint or set of plans for building an apartment; the container is the actual, fully-built building.

# How to create my own image?
Dockerfile!
- It consists of instruction and argument
	- `FROM Ubuntu` : Start from a base OS or another image
	- `RUN apt-get update`
	- `COPY . /opt/source-code`: copy source code
	- `ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run`: specify entrypoint (running command)

## Basics
- `docker pull <images>`: e.g., `docker pull nginx`
- `docker images` : list images I have
	- This is an alias of `docker image ls`
	- show: nginx:latest image
- Delete docker images:
	- `docker rmi <name>`: remove images
	- Need to make it sure no containers are using this image

## Dockerfile
To build our own image we create a special file known as a Dockerfile that defines the steps to create and run the custom image.
- Build own images by creating _dockerfile_

### Create Dockerfile
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

### CMD vs Entrypoint
- Containers are not meant to host OS
- Containers are meant to host processes
	- Once the task is completed, containers exit. 
- You can specify a command. e.g., `CMD sleep 5`
	- How to change/specify arguments
	- _Entrypoint_
- Entrypoint allows us to give argument rather than hard specified. 
- To set a default value we need to mix both of them
```
ENTRYPOINT ["sleep"]
CMD ["5"]
```


### Docker Build
- Create an _image_ from the _Dockerfiile_
	- `docker build --tag website:latest .`  : docker file is inside, so just use `.`
		- `--tag` or `-t`
		- `docker ima**ge ls` : check 
		- `website`: name / `latest`: tag
- Now we don't have to create a volume. Simply run
	- `docker run --name website -d -p 8080:80 website:latest`
	- You can check by using your browser

### Ignore Files 
- Create `.dockerignore` : similar to `.gitignore`
	- `.git`
	- `Dockerfile`
	- `*.gulp.js`
	- `node_modules`
	- `dir/**`

## Caching and Layers
Say that you are updating user information in `index.js`, then you have to build a new image and run a container.  We shouldn't waste time for simply updating some information. To avoid this, we can leverage caching.  A simple trick is to add caching file before adding all files.
```
FROM node:latest
WORKDIR /app
ADD package*.json ./
RUN npm install 
ADD . .
CMD node index.js
```

## [Alpine](https://hub.docker.com/_/alpine) for Minimal Image

> [Alpine Linux](https://alpinelinux.org/) is a Linux distribution built around [musl libc](https://www.musl-libc.org/) and [BusyBox](https://www.busybox.net/). The image is only 5 MB in size and has access to a [package repository](https://pkgs.alpinelinux.org/) that is much more complete than other BusyBox based images. This makes Alpine Linux a great image base for utilities and even production applications. [Read more about Alpine Linux here](https://alpinelinux.org/about/) and you can see how their mantra fits in right at home with Docker images.

When you pull or create standard docker images, their size is quite huge.  

### Pulling Alpine Images
- `docker pull node:alpine` : Alpine version of node
	- `docker image ls` : to check its size... it is significantly smaller than the standard node docker image `node:latest`.
- `docker pull nginx:alpine`

## Tags and Versions
- Tags allows you to control image version
- Avoids breaking changes 

### Tagging containers
- `docker tag website:latest website:1`
	- They do have the same content
### Running containers with tags
- For example, 
	- `docker run --name website-2 -d -p 8080:80 website:latest`
	- `docker run --name website-1 -d -p 8080:80 website:1`

## Docker Registries 
- `docker pull/push <image>`

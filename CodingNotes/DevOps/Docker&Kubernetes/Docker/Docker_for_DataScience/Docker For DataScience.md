# Introduction
Docker provides a simply way, called container, to _package application with all the necessary dependencies and configurations,_ which is _easy to share and move to any environment_. 

## Docker vs Image
Let's say we want to build an app. Then, we are going to containerize the dependencies and the configurations of the app, which is a stack of _images_. For instance, the first image would be a Linux base image and the second one is SQL and so on. In short, containers are layers of image.  

A Docker image is a read-only template that describes how to create a Docker container. 
- The image is the instructions 
- The container is the actual running instance of an image. 
An analogy of an apartment, an image is the blueprint or set of plans for building an apartment; the container is the actual, fully-built building.

## Docker vs VM
- Docker only models an application layer of an OS, so the image size is smaller and runs faster than VM. 
- Virtual machine can be installed on any OS. Thus, there is no compatibility issue.
- However, Docker may have the compatibility issue depends on the OS. 

# Dockerfile

```dockerfile
FROM basename
COPY
WORKDIR
RUN
CMD
```

For instance,
```dockerfile
FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
```
- copy the local dir to `/app`

Then, 
- `docker build -t appname .`: install a docker image
- `docker images`: to list existing images
- `docker run -p 5000:5000 welcome-app`:
	- `--tag` or `-t`


# Docker Compose


Docker compose is for managing multiple containers that may interact between them.
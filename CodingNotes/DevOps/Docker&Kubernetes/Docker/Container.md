---
tags:linux, docker, kubernetes 
---

## Check Status
- `docker ps` 
	- List running containers
- `docker ps -al`
	- `-a`: Show all info
	- `docker ps --format=ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n`
		- Allows to make it more readable
		- We can keep this info by
			- `export FORMAT=ID\t{{.ID}}\nNAME\t{{.Names}}\nImage\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n`
			- `docker ps --format=$FORMAT`

## Run Container
- `docker run nginx:latest` : latest is the tag
	- This runs a container, then just open a new termianl and run:
	- `docker container ls` : show conatiners
	- Quit the container by simply `CTRL+C`
	- If docker cannot find an image, then it will try to pull it. 
- By default Docker runs containers in the attached mode, so it doesn't wait for prompt
- If we just want to feed an argument, then just use `docker run -i` , parameter but it cannot wait for prompt. 
	- `docker run -it`: `-t` is terminal
- `docker run -d nginx:latest` : run the container in the detached (background) mode. 
	- `docker attach <container>`: Attack back i.e.,  run in the foreground mode
- `docker run -d -p 8080:80 nginx:latest`
	- In my browser: `localhost: 8080` or `http://localhost:8080/dist/index.html`
	- `-p`: port
- `docker run -d -p 8080:80 -p 3030:80 nginx:latest`
	- We can map more than one port
- Once we run the container, we can access to my application by a port.

## Stop & Resume Container
- `docker stop <Container Name/ID>` : stop container
	- In case you can still see the container in your browser by localhost, check the cache setting in your browser.
	- List all numeric container ids:
		- `docker ps -aq`
- Note that we just stopped it, but haven't removed it, so we can resume it. 
	- `docker start <CONTAINERID/NAMES>`
 
## Delete Container
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
 
## Naming Containers
- `docker run --name <NAME> -d -p 8080:80 nginx:latest`

## Volumes
Volumes allow to share data (Files and Dir). 
- Between host and container 
- Between containers 
- If you want to keep your data outside container, then you need to create a volume (or vice versa)

### Host and Container
- `docker run --name website -v $(pwd):/usr/share/nginx/html:ro -d -p 8080:80 nginx:latest`
	- By running this command, the container can bring files inside the `PWD`.
	- `website` is my container's name 
	- `-v` : create a volume named by `PWD`
	- The files will be stored at `/usr/share/nginx/html`
- To get files from the container 
	- `docker exec -it <container> bash`: this command activate bash command. 
		- `it`: interactive terminal
	- We can use bash commands freely e.g., `ls`.
	- However, we cannot write something inside `html` directory in container, since it is the `readonly` directory. To resolve this issue, we have to run it without `ro` argument. 
		- `docker run --name website -v $(pwd):/usr/share/nginx/html -d -p 8080:80 nginx:latest`

### Between Containers
- `docker run --name website-copy --volumes-from website -d -p 8081:80 nginx`
	- It creates a connection between `website-copy` and `website`

## Docker Environment Variables
- `docker run -e APP_COLOR=blue simple-webapp-color`

## Docker Inspect/ Logs
- `docker inspect <container>`
	- We can also inspect environment variables
- `docker logs <container>`



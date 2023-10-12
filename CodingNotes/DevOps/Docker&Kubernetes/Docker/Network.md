![[Docker_Network_1.png]]

- Port is the gate for our file system.
- Host and container are independent system, so we cannot directly access to the container by port 80:
	- Thus, we need to connect the ports of the host and the container by running the command: `docker run -p 80:80 httpd`
	- This connection is called _port forwarding_

When we install docker, it automatically creates three default networks:
- Bridge: private internal network. All containers are attached to this by default.
- None: allows to access externally
- Host: 

[Reference](https://techblog.geekyants.com/understanding-docker-networking-1)

## Basics
- `docker inspect <container>`
- 

## Bridge
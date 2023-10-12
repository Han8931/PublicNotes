---
tags: network, web
---

For communication between devices, ip address (internet protocol address) is necessary. 
- IPv4
- IPv6 : ipv4 was not enough to cover new users

## Router

### IP Address
To use the internet, every device has to have an ip address. However, to cover multiple devices such as smart phone, laptop, and desktop, we need to have multiple ip addresses. To alleviate the issue, we can use only one ip address (59.6.66.238) with a router. 
![[router.png]]
- WAN (wide area network): This is connected to the internet. 
	- _Public IP address_: 59.6.66.238
- LAN (local area network): Router assign an IP address for each device, including even the router
	- Router (or gateway) address: 192.168.0.1
	- These IP addresses are _private IP address_. 
		- Private IP address has 3 classes:
		-   Class A: `10.0.0.0` to `10.255.255.255`
		-   Class B: `172.16.0.0` to `172.31.255.255`
		-   Class C: `192.168.0.0` to `192.168.255.255`
	- An IP address within these ranges is therefore considered non-routable, as it is not unique. Any private network that needs to use IP addresses internally can use any address within these ranges without any coordination with IANA or an Internet registry. Addresses within this private address space are only unique within a given private network.

## Network Address Translation (NAT)

An user with private IP address may request to send some info through router. Then, router translates (changes) the private IP address (192...) to the public IP address (59.6...) by using NAT while keeping the private IP address. Subsequently,  the router sends the info to the target IP. When it receive some data from the target then, it leverages the memorized private ip address. 

## Port
- `0-1023`: Well known port
	- For instance, 80 is for HTTP, 22 for SSH. 
	- Avoid using a port in this range 
	 - in total 65535 ports are available
		- For example 8080 port can be used for a personal purpose.

## Port Forwarding

![[port_forwarding.png]]

## Dynamic and Static IP Address 

- ISP (Internet Service Provider) would assign an IP address for me. 
- However, if I don't use the internet for a long time, then ISP would retrieve my IP address and assign for another user. This is called _dynamic IP address_. This is mainly because, the IPv4 has no enough IP address range. 
- However, dynamic IP address is not appropriate for server computers, since dynamic IP addresses keep changing. To address this issue, _static IP addresses_ can be used. However, this is not free. 

## Dynamic Host Configuration Protocol (DHCP)
- DHCP client (user) announces that I need an IP address with its MAC address.
	- MAC address: every device has its own physical address
- Then, DHCP server (router) assigns an IP address. 
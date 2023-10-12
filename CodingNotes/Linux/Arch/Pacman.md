---
tags: linux, pacman
---
Pacman is a package manager for Arch Linux. 

## Config 
- Parallel download:
	- `sudo vim /etc/pacman.conf`
	- `ParalleldDownloads=5 # Uncomment this line`
- Install from git
	- `git clone <pkgname>`
	- `makepkg -si`
- Create a installed package list: `pacman -Qqen > pkglist.txt`
	- To install: `pacman -S - < pkglist.txt`

## Install Pkg
- `sudo pacman -S <pkg-name>`
	- `-S`: install
- `sudo pacman -Syu`
	- `-y`: sync database (sudo apt-get update)
	- `-u`: upgrade (sudo apt-get upgrade)
	- `-w`: download pkgs
	- `-s`: search pkg
 
## Remove Pkg
 - `sudo pacman -R <pkg-name>`: Remove pkg
	 - `-s`: remove dependencies. Note that it might crush the dependencies of other program.
	 - `-n`: remove system config file. It is not your config file. 
 - `sudo pacman -Rns <pkg-name>`: this is the _best practice_ to remove pkg. 

## List Installed Pkg
- `sudo pacman -Q`: list all installed pkg
- `sudo pacman -Qe`: list pkgs you manually installed
	- `-q`: remove version info when pacman lists pkgs
- `sudo pacman -Qm`: list installed AUR pkgs
- `sudo pacman -Qdt`: list unneeded dependencies (orphans)

## Remove Old Version of Pkg
- `sudo pacman -Sc`: remove obsolete pkg

## Install AUR packages using Git
- `git clone <clone URL>`
- `makepkg -si`

---
tags: linux, arch
---
# Basics

## Package management

## yay
- Sudo timeout issue
	- `yay -S [pkg] --sudoloop # Prevent timeout`

## TexLive
[ArchWiki TexLive](https://wiki.archlinux.org/title/TeX_Live)
- Install all packages listed in the website. 
	- Core:  `sudo pacman -Syyu texlive-most texlive-bin`
- __Never__ install `texlive-full`

## NeoVim
- Install`xclip` for yaking to clipboard in neovim 

## Korean Language Font
- `yay -S ttf-nanum`

## Audio
- `sudo usermod -aG audio han`
	- `-aG`: add to Group
- `sudo alsactl init`


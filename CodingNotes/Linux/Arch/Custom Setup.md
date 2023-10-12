# Post-Installation
- `sudo pacman-mirrors --fasttrack`
- `pacman -Syyu`

- TextLive (latex)
	- `yay -S texlive-full --sudoloop`
	- To prevent sudo timeout (`--sudoloop`)
- Korean keyboard setting:
	- `sudo pacman -S ibus-hangul`
- LF file manager image previewer
	- `yay -S ctpv-git`
- NordVPN: `nordvpn-bin` (AUR)
- PDF, epub viewer: `zathura-pdf-mupdf`
	- Calibre
- Firewall: `ufw`
- SSH: `openssh-server`
- Neovim:
	- coc installatiion: `yarn`, `npm`
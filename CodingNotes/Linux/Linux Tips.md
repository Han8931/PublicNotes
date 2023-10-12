---
tags: linux, terminal
---
## Mount Android
- `simple-mtpfs -l`: list devices
- `simple-mtpfs --device <number> <mount_dir>`: list devices
- `fusermount -u <mount_dir>`: unmount device
- Just use Android-file-transfer

## PDF related
### pdfgrep
- `pdfgrep -HiR <patter> <dir>`
	- `-R`: recursively
### pdftotext
- `pdftotext <pdf>`: change pdf to txt
- `pdftotext -htmlmeta <pdf>`: extract html meta data
- `pdftotext -l 1 -htmlmeta <pdf>`: extract html meta data from the only first page. 
	- `-l`: specify the last page number to extract

## Bluetooth
- Best way is to use [[bluetuith]] 
For Logitech proucts, just install `solaar`:
- `pacman -S solaar`
- Then type `solaar`

Command line based approaches:
- check: `sudo systemctl status bluetooth`
- First, type `bluetoothctl`
	- Scan devices: `scan on`
	- List all known devices (Paired): `devices`
	- Power the Bluetooth controller on or off: `power [on|off]`
	- Pair with a device `pair [mac_address]`
	- Remove a device `remove [mac_address]`
	- Connect to a paired device `connect [mac_address]`
	- Disconnect from a paired device `disconnect [mac_address]`
	- Display help `help`

## Check WiFi Password
- `cd /etc/NetworkManager/system-connections/ `
	- Run it in `su` .
 
## Inputs
- Disable touchpad
	- `xinput` : list all input devices
	- `xinput enable/disable [dev ID]`
 
## Format USB
- `sudo mkfs.vfat -n "USB" -I /dev/sdc`
	- make file system fat32, namely USB

## Create a Bootable USB
- `dd if=<iso image> of=<usb path> status=progress`
	- if: input file
	- of: output file: for instance `/dev/sda`
	- Run this command with `su`
 
## Wi-Fi Connection
- `nmcli connection show`: list wifi
- `nmcli device wifi connect <wifiname> password <passwd>`

## Mime Type
- `xdg-mime query filetype <file>`

## Mount USB drive with write permissions for everyone or specific user
- `sudo mount /dev/sdb2 /home/storage -o umask=000`

## Printer
### Two sided print
- `lpr`: send a job to a printer
- `lpq`: print job queue 
- `lpr -P [printer name] -lw -o sides=two-sided-long-edge [filename]`





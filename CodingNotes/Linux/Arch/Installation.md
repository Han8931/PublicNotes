---
tags: linux, arch
---

# Preparation
## Bootable USB 
- `dd if=<iso image> of=<usb path> status=progress`
	- if: input file
	- of: output file: for instance `/dev/sda`
	- Run this command with `su`

# Installation
## WiFi Connection
- `iwctl`
- `device list`
- `station <wlan> scan`
- `station <wlan> get-networks`
- `station <wlan> connect <wifi-name>`
- `station <wlan> show`
- `exit`

## Check If UEFI or Not
- `ls /sys/firmware/efi/efivars`: if it shows error then it uses traditional BIOS

## Check Internet Connection
- `ping google.com`
	- Note that you have to turn off `iwctl` by `exit` command first

## Check Time
- `timedatectl set-ntp true`

## Partition
- `fdisk <target disk>`
	- Target disk to install Arch Linux. The target can be identified by using `lsblk` command
	- For example, `fdisk /dev/sda`
- Then, type `d`: to delete the disk
	- To clean the disk
- Then, type `p` (print) to see the current partition table. 
- Use the `n` (new) command to create a new partition. 
	- Then, just type `Enter` to use a default setting.
- Set the partition size like `+25G` or `+100M`
	- You can skip the first sector, but type the size at the last sector
	- Remove the signature. 
 
> __Be careful__, when you try to create the last partition, Arch would ask you to create a extended partition, but you have to create a primary partition, so don't type `Enter`.

### Four Primary Partitions
- boot: `+200M`
- swap
	- 50% of your RAM size.
	- `+8G`
- root
	- At least `+25G`
- home
	- If you don't set the size of your partition size, then it will use the rest of your disk. 
	- 
- **Once you have done everything, type `w`, which means _write_.** This command will create partitions.

> Artix linux installation guide from Luke created only two partitions.  one for +1G, which is boot, and the other one gets the remaining space.

### Mount Partitions

#### Create File Systems
- boot: `mkfs.ext4 <boot partiton>`: e.g., /dev/sdb1
- root: `mkfs.ext4 <root partiton>`: e.g., /dev/sdb1
- home: `mkfs.ext4 <home partiton>`: e.g., /dev/sdb1
- swap: `mkswap <swap partiton>`: e.g., /dev/sdb1

#### Mount File Systems
- swap: `swapon </dev/sdb2>`
- root:  `mount /dev/sdb3 /mnt`
	- Check by `ls /mnt` then you will see `lost+found`
- boot: 
	- For UEFI machine, FAT32 has to be used. 
		- `mkfs.fat -F32 <boot partition>`
	- `mkdir /mnt/boot`
	- `mount /dev/sdb1 /mnt/boot`
- home: `mkfs.ext4 <home partiton>`: e.g., /dev/sdb1
	- `mkdir /mnt/home`
	- `mount /dev/sdb2 /mnt/home`

### Encrypt Partition with Artix
- `cryptsetup luksFormat <partition>`
- To decript, 
	- `cryptsetup open <partition> <SomeName>`
- For encrypted partition :
	- `mkfs.btrfs <encripted one>`
- And mount partions
	- `mount <boot> /mnt/boot`
	- `mount <another partition> /mnt`
 
## FastMirrorLIst
- `vim /etc/pacman.d/mirrorlist`:
	- Just choose mirror near to you and move it to the top

## pacstrap /basestrap
This is the step where Arch Linux will be actually installed. 

For Arch
- `pacstrap /mnt base base-devel vim linux linux-firmware`: install things you wanna use immediately. 
	- Install base packages...
For Artix
- `basestrap -i /mnt base base-devel runit elogind-runit linux linux-firmware grub networkmanager networkmanager-runit cryptsetup lvm2 lvm2-runit neovim vim`

## fstab
Mount partitions automatically
- `vim /etc/fstab`: you can check what Linux is trying to load. We don't have to manually write them down.  Instead,
- `genfstab -U /mnt >> /mnt/etc/fstab`
	- `-U`: use UUID by default. 
	- `vim /mnt/etc/fstab`: to check 

## arch-chroot /artix-chroot
Arch
	- So far we have been running arch in USB, but by the command below, we will run arch in `mnt`
	- `arch-chroot /mnt`: Now we are in the `/mnt`
		- `vim /etc/fstab`
Artix
	- `artix-chroot /mnt bash`

## Network Manager
- `pacman -S networkmanager`
- `systemctl enable NetworkManager`: enable it whenever you log in

## Grub
- Install GRUB (bootloader): `pacman -S grub`
	- Install GRUB on a BIOS: `grub-install --target=i386-pc /dev/<target>`
		- or simply  `grub-install /dev/sda`
  
	- Install GRUB on an UEFI: `grub-install ????????` **I have to figure it out this command**
- Create a grub config file: 
	- `grub-mkconfig -o /boot/grub/grub.cfg`

## Set Password
- `passwd`: root password

## Locale
- `vim /etc/locale.gen`: uncomment your locale (two lines)
- `locale-gen`: update change
- `vim /etc/locale.conf`: put the lines below and save this
	- `LANG=en_US.UTF-8`
 
### Timezone:
- `ls /usr/share/zoneinfo/`
- `ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`
- You can check 
	- `ls -l /etc/localtime`

## Name Your Computer
- `vim /etc/hostname`: name your computer

## Exit and Reboot
- `exit`: back to USB drive
- `umount -R /mnt`: recursively unmount
- `reboot`

# Post Installation
## Initial accout: `root`
## Add User
- `useradd -m -g wheel han`
	- The wheel group is a special user group used on some Unix systems, mostly BSD systems, to control access to the su or sudo command.
	- `usermod -aG wheel,audio,video,storage <user>`: `<user>` is `han`

- `passwd han`: to change passwords

### sudoers
- `vim /etc/sudoers`: list all diff permissions for users and groups
- Add sudo user by 
	- `han ALL=(ALL:ALL) ALL`
- Some optional configs:
	- `Defaults !tty_tickets`
	- `wheel ALL=(ALL) NOPASSWD: /usr/bin/shutdown,restart,pacman -Syu`

## X.org
In order to have a graphical environment, we need `X.org`
- `pacman -S xorg-server xorg-xinit`
- You can start `X` by `xinit` or `startx`.
	- To do this you need to install Window manager first.
	- `pacman -S i3 dmenu rxvt-unicode`
- Note that you may have to connect to internet again by `nmtui`

## Fonts
- `pacman -S ttf-linux-libertine ttf-inconsolata`
- Or just `pacman -S noto-fonts`
- Check your fonts manually in:
	- `~/.config/fontconfig/fonts.conf`

## Auto Start i3
- In `~/.xinitrc`, put 
```
exec i3
startx
```

## TTY
- `Ctrl+Alt+F(2-3-4...)`: F means function key

## Display Manager 

This is optional
- `sudo pacman -S lightdm lightdm-gtk-greeter`
- `sudo systemctl enable lightdm.service`


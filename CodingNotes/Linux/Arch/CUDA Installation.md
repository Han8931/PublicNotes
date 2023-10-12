[Reference](https://jaggu-iitm.medium.com/setting-up-deep-learning-with-cuda-tensorflow-and-keras-on-arch-linux-with-dual-gpu-nvidia-gpu-82963d2ecb75)

1. `sudo pacman -S cuda cudnn`
2. `sudo pacman -S nvidia-dkms nvidia-utils`
3. If you get an error, then `sudo pacman -Ss linuxXX(X)-headers`
	- XX could be 515 or 61 for example.
	- It should be obvious these stand for 5.15 and 6.1 kernels. 
	- Type `uname -r` in terminal to get your kernelversion. 
	- Then install it with `sudo pacman -S linux(yourversion)-headers`
- If there are any errors run the above commands to update.
- Then, reboot

`pip3 install torch torchvision torchaudio`


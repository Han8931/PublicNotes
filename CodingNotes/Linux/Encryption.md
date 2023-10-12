
## Why Disk Encryption? [Permalink](https://fernandocejas.com/blog/engineering/2020-12-28-install-arch-linux-full-disk-encryption/#why-disk-encryption)

**There is a short answer for this: Security**. In a time where **(almost) all our information is binary** and for instance, our lives, are mostly inside of devices, I personally want to ensure that **my sensitive information is hard to get** even if my laptop lands on the street, due to it being stolen or lost (hopefully not but **never say never…**).

So it is time to jump deeper in the **core of this article**:

The result is going to be a **Full Arch Linux installation with Disk Encryption(FDE)**.

### What is Block Device Encryption? [Permalink](https://fernandocejas.com/blog/engineering/2020-12-28-install-arch-linux-full-disk-encryption/#what-is-block-device-encryption)

**Block device encryption encrypts/decrypts the data transparently as it is written/read from block devices, the underlying block device sees only encrypted data.** To mount encrypted block devices we must provide a passphrase to activate the decryption key.

_Some systems require the encryption key to be the same as for decryption, and other systems require a specific key for encryption and specific second key for enabling decryption._
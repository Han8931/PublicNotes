---
tags: gpg, pass
---

# What is GPG?
>It is one of the most well-known software for the encryption and digital signatures verification call PGP --Pretty Good Privacy.  **GPG (GNU privacy guard)** is an open-source implementation of the OpenPGP protocol. It’s a free alternative to the **PGP** program. Then what is PGP? PGP (Pretty Good Privacy) is an encryption program developed in 1991 by Phil Zimmermann.

PGP and GPG are commonly used for two things.

-   **Encryption**: encrypt emails and files like Edward Snowden does every day, so bad actors can’t read your encrypted emails and files.
-   **Signing**: create digital signatures for signing documents. You can also use it to digitally sign all your outgoing emails, so the recipient can know the email hasn’t been tampered with. The software repository of your Linux distribution is also signed by a PGP key, so you can be sure that you are not downloading malware when running commmand `sudo apt update` or `sudo dnf update`.

- `gpg --full-gen-key` : to generate a gpg key
	- Default/ 4096/ 
- `gpg -k` : list public keys

## Encrpypt / Decrypt Files 
- `gpg -r <myemail> -e <filename>`:
	- `-r`: recipient 
- `gpg -d <file.gpg>`

## Some Commands
### Edit my keys
- `gpg --edit-key <myemail>`
	- `key 1`
	- `expire`
	- `save`
- To change your passphrase
	- `gpg passwd <myemail>`

### Revoke my key


### List My Public Key
- `gpg --list-sigs user-id`

### Export My Public Key
- `gpg --armor --export user-id > pubkey.asc`

### Export My Private Key
- `gpg --export-secret-keys --armor user-id > privkey.asc`

## GPG Key for GitHub

### How to add GPG key to GitHub

- `gpg --list-secret-keys --keyid-format LONG`
	- Copy the ID of the generated key's fingerprint
- `gpg --armor --export <user-id(my email address)>`

## Generate SSH key
- `ssh-keygen -t rsa` or simply `ssh-keygen`
	- `id_rsa` : private key
	- `id_rsa.pub` : public key
 
### SSH key for Git
- Go to SSH and GPG keys in the setting menu of GitHub
- Just paste your public key
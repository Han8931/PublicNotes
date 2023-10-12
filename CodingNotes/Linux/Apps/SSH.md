## Generate SSH key
- `ssh-keygen -t rsa` or simply `ssh-keygen`
	- `id_rsa` : private key
	- `id_rsa.pub` : public key
 
## SSH key for Git
- Go to SSH and GPG keys in the setting menu of GitHub
- Just paste your public key

## Auto Login
- You just have to simply paste your public key to `authorized_keys` in the ssh directory.
- However, a simple way is
	- `ssh-copy-id user@ip-addr`: this command generates the authorized_keys file automatically.

### Reference
- [Ref](https://opentutorials.org/module/432/3742)
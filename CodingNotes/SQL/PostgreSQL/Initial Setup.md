---
tags: postgresql, sql, database
---
[Reference: How to install PostgreSQL and PgAdmin in Manjaro?](https://linuxhint.com)

# Install PostgreSQL
- Install the postgresql package. It will also create a system user called _postgres_. You can now switch to the _postgres_ user using a privilege (e.g., `sudo`).  
	- `sudo pacman -S postgresql` 
- You can switch to the PostgreSQL user by executing the following command: 
	- `sudo -iu postgres`
	- `-i`: login
	- `-u`: user
- Before PostgreSQL can function correctly, the database cluster must be initialized:
	- `[postgres]$ initdb -D /var/lib/postgres/data` or
	- `[postgres]$ initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data --data-checksums`
	- Note that commands that should be run as the _postgres_ user are prefixed by `[postgres]$` in this article.
- By default, the PostgreSQL service is managed by systemd. You can start the PostgreSQL service with the following command: 
	- `$ systemctl start postgresql`
	- `$ systemctl status postgresql`
- To enable the PostgreSQL service to start after the system reboots, run the following command:
	- `$ systemctl enable postgresql`
- To use PostgresSQL, just type:
	- `$ psql -U postgres`
	- After accessing the postgres shell, type “**\password**” to set a password. Choose the password and enter again to confirm:
	- `\password`

# Install PgAdmin
- Make the essential directories, **/var/lib** and **/var/log** for **pgadmin.** Where **/var/lib** directory is used by the server applications to store data and **/var/log** files contains the log files. To create these files, use the below-mentioned command.
	- `$ sudo mkdir /var/lib/pgadmin  `
	- `$ sudo mkdir /var/log/pgadmin`
	- `$ sudo chown $USER /var/lib/pgadmin  `
	- `$ sudo chown $USER /var/log/pgadmin`
- Create the Python-based virtual environment by issuing the command written below.
	- `python3 -m venv pgadmin4`
- Activate venv:
	- `source pgadmin4/bin/activate`
- `pip install pgadmin4`
- `cd pgadmin4`
- `pgadmin4`
- ou must observe that the output is notifying you to navigate to address [**https://127.0.0.1:5050**](https://127.0.0.1:5050/)**.** Enter the address in any browser and you would observe the following interface.
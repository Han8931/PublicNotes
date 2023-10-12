---
tags: sql, database, sqlite, python
---
### Connect to DB
- `conn = sqlite3.connect('customber.db')
	- This creates a empty database
 
### Create a table
- We first need to create a cursor
	- `c = conn.cursor()`
- `CREATE TABLE`: this statement is for creating a table.
```sql
c.execute("""CREATE TABLE customers (
          first_name text,
          last_name text,
          email text
          )
          """)
``` 
- SQLite has five different DATATYPE :
	- `NULL`
	- `INTEGER`
	- `REAL`
	- `TEXT`
	- `BLOB`: can be any type of data, e.g., image, mp3, and so on...
 


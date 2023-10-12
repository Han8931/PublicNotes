---
tags: postgresql, sql, database
---
- `\q`: quit
- `\c`: connect to database
- `<C-l>`: clear screen
	- `\! clear`
- `\?`: help 
- `\x`: expanded display 
- `\copy (<SQL Command>)`:  Put a SQL command inside the parentheses. 

## RUN Script
`\i <name.sql>`: run a sql script

## CREATE TABLE
```sql
test=# CREATE TABLE person (
test(# id INT,
test(# first_name VARCHAR(50),
test(# last_name VARCHAR(50),
test(# gender VARCHAR(7),
test(# date_of_birth DATE );
```
- `\d`: display relations
	- `\d person`: display table info
	- `\dt`: display only tables

### DROP TABLE
You can remove table by 
- `DROP TABLE <tablename>`

#### A Better Way to Create A Table
```sql
CREATE TABLE person (
id BIGSERIAL NOT NULL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
gender VARCHAR(7) NOT NULL,
date_of_birth DATE NOT NULL,
email VARCHAR(150));
```
- `PRIMARY KEY`: A primary key is a column or a group of columns used to identify a row uniquely in a table. You define primary keys through primary key constraints. Technically, a primary key constraint is the combination of a not-null constraint and a UNIQUE constraint. A table can have one and only one primary key. It is a good practice to add a primary key to every table. When you add a primary key to a table, PostgreSQL creates a unique B-tree index on the column or a group of columns used to define the primary key.
- `NOT NULL`: When a person is added into this table it shouldn't be null value. 

### INSERT INTO
```sql
INSERT INTO person(
first_name,
last_name,
gender,
date_of_birth)
VALUES ('Anne', 'Smith', 'FEMALE', date '1988-01-09');
```

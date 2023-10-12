---
tags: sql, database
---

## SELECT

The SQL SELECT statement is used to select (retrieve) data from a database table.

```sql
-- select first_name from Customers table 
SELECT first_name
FROM Customers;

-- select all columns from Customers table 
SELECT *
FROM Customers;
```

### Select: query data from a single table
You can use the `SELECT` statement to perform a simple calculation as follows:
- `SELECT 1+1;`
You can use multiple expressions in the `SELECT` statement as follows:
```sql
SELECT 
10/5,
2*4;
```

### Where 
The `WHERE` clause is an _optional clause_ of the `SELECT` statement. It appears after the `FROM` clause as the following statement:

The search condition in the `WHERE` has the following form:
- `left_expression COMPARISON_OPERATOR right_expression`
	- `WHERE column_1 = 100; `
	- `WHERE column_2 IN (1,2,3);`
	- `WHERE column_3 LIKE 'An%'; `
	- `WHERE column_4 BETWEEN 10 AND 20;`
 
```sql
SELECT name, milliseconds, bytes, albumid FROM tracks WHERE albumid = 1;
SELECT name, milliseconds, bytes, albumid FROM tracks WHERE albumid = 1 AND milliseconds > 250000;

-- select all columns from the customers table with last_name 'Doe' 
SELECT *
FROM Customers
WHERE last_name = 'Doe';
```


#### Combining Multiple Operators 
```sql
-- select customers who live in either USA or UK and whose age is less than 26
SELECT *
FROM Customers
WHERE (country = 'USA' OR country = 'UK') AND age < 26;

-- exclude customers who are from the USA and have 'Doe' as their last name
SELECT *
FROM customers
WHERE NOT country = 'USA' AND NOT last_name = 'Doe';
```

### Distinct
The `DISTINCT` clause is an optional clause of the  `SELECT` statement. The `DISTINCT` clause allows you to remove the duplicate rows in the result set.

- First, the `DISTINCT` clause must appear immediately after the `SELECT` keyword.
- Second, you place a column or a list of columns after the `DISTINCT` keyword. If you use one column, SQLite uses values in that column to evaluate the duplicate. In case you use multiple columns, SQLite uses the combination of values in these columns to evaluate the duplicate.

SQLite considers `NULL` values as duplicates. If you use the`DISTINCT` clause with a column that has `NULL` values, SQLite will keep one row of a `NULL` value.

>Suppose you want to know the cities where the customers locate, you can use the `SELECT` statement to get data from the `city` column of the `customers` table as follows:
```sql
SELECT city FROM customers ORDER BY city;
```
- The above code will return unique cities.  
- `SELECT DISTINCT city, country FROM customers ORDER BY country;`

```sql
-- select rows if the first name and country of a customer is unique
SELECT DISTINCT country, first_name
FROM Customers;
```
- It will select rows if the combination of `country` and `first_name` is unique.

#### DISTINCT  with Count
```sql
-- count the unique countries where customers are from 
SELECT COUNT(DISTINCT country)
FROM Customers;
```

> Note that `SELECT UNIQUE` is an obsolete method. 

#### SQLite `SELECT DISTINCT` with `NULL` example
- `SELECT company FROM customers;`
- `SELECT DISTINCT company FROM customers;`


### AS
The `AS` keyword is used to give columns or tables a temporary name that can be used to identify that column or table later.
```sql
SELECT first_name AS name
FROM Customers;
```

We can combine data from multiple columns and represent it in a single column using the `CONCAT()` function. For example,
```sql
SELECT CONTACT(first_name, ' ', last_name) AS full_name
FROM Customers;
```
Here, the SQL command selects `first_name` and `last_name`. And, the name of the column will be `full_name` in the result set.

### Limit
The `LIMIT` keyword in SQL allows you to specify the number of records to return in a query.

```sql
SELECT
	trackId,
	name
FROM
	tracks
LIMIT 10 OFFSET 10;
```

> Note that `LIMIT` is not a standard SQL keyword. `FETCH` does the same thing. 

#### SQL LIMIT With OFFSET Clause

The `OFFSET` keyword is used with `LIMIT` to specify the starting rows from where to select the data. For example,
```sql
-- LIMIT 2 selects two results
-- OFFSET 3 excludes the first three results

SELECT first_name, last_name
FROM Customers
LIMIT 2 OFFSET 3;
```
Here, the SQL command selects **2** rows starting from the fourth row. `OFFSET 3` means the first **3** rows are excluded.

### Top
```sql
SELECT TOP 2 first_name, last_name
FROM Customers;
```

### IN
The `IN` operator is used with the `WHERE` clause to match values in a list.

```sql
-- select customers from the USA
SELECT first_name, country
FROM Customers
WHERE country IN ('USA');
```
Here, the SQL command selects rows from the `Customers` table whose `country` value is `'USA'`.

```sql
-- select rows if the country is either USA or UK
SELECT first_name, country
FROM Customers
WHERE country IN ('USA', 'UK');
```
Here, the SQL command selects rows if the country is either **USA** or **UK**. Note that the `IN` operator ignores duplicate values in the list. For example, take a look at the code below.

#### SQL IN Operator With Columns
```sql
-- select rows with value 'USA' in the country column
SELECT first_name, country
FROM Customers
WHERE 'USA' IN (country);
```

#### SQL NOT IN Operator
The `NOT IN` operator is used to exclude the rows that match values in the list. It returns all the rows except the excluded rows. For example,
```sql
-- select rows where country is not UK or UAE
SELECT first_name, country
FROM Customers
WHERE country NOT IN ('UK', 'UAE');
```

#### SQL IN Operator With Subquery
Suppose we only want the details of those customers who have placed an order. Here's how we can do that using a subquery,
```sql
-- select only those customers who have placed an order
-- the subquery is enclosed within parentheses after the IN keyword
SELECT customer_id, first_name
FROM Customers 
WHERE customer_id IN (
  SELECT customer_id
  FROM Orders
);
```
Here, the SQL command

1. selects `customer_id` from the `Orders` table using the subquery,
2. selects rows from the `Customers` table where `customer_id` is in the result set of the subquery i.e., if the `customer_id` is also in the `Orders` table.

### Between
```sql
-- select rows where the amount is between 200 and 600
SELECT item, amount
FROM Orders
WHERE amount BETWEEN 200 AND 600;
```

#### SQL BETWEEN OPERATOR With Texts
```sql
-- select rows where items begin with letters between 'I' and 'L'
-- exclude all items beginning with 'L' followed by other characters
SELECT item, amount
FROM Orders
WHERE item BETWEEN 'I' AND 'L';
```
Here, the SQL command selects all orders where the item names begin with letters between **I** and **L**.


### IS NULL / IS NOT NULL Operators
The following statement attempts to find tracks whose composers are NULL:
**Incorrect NULL check:**
```sql
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer = NULL;
```
It returns an empty row without issuing any additional message, since It’s _not valid to use the NULL this way_.

**Correct NULL / NOT NULL check:**
```sql
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NULL // or 
    Composer IS NOT NULL 
ORDER BY 
    Name;   
```

#### IS NULL With COUNT()
We can use the `COUNT()` function with `IS NULL` to count the number of rows with an empty field. For example,
```sql
SELECT COUNT(*)
FROM Employee
WHERE email IS NULL;
```

### SQL MAX / MIN Function

```sql
SELECT MAX(age) 
FROM Customers;
```

```sql
SELECT MIN(age) 
FROM Customers;
```

#### Aliases With MAX() and MIN()

In the above examples, the field names in the result sets were `MIN(age)` and `MAX(age)`.

It is also possible to give custom names to these fields using the `AS` keyword. For example,

```sql
-- use max_age as an alias for the maximum age
SELECT MAX(age) AS max_age
FROM Customers;
```
Here, the field name `MAX(age)` is replaced with max_age in the result set.

#### MAX() and MIN() in Nested SELECT

As we know, the `MAX()` function returns the maximum value. Similarly, the `MIN()` function returns the minimum value.

However, if we want to select the whole row containing that value, we can use the nested `SELECT` statement like this.

```
-- MIN() function in a nested SELECT statement

SELECT *
FROM Customers
WHERE age = (
    SELECT MIN(age)
    FROM Customers
);
```

### COUNT
```sql
-- returns the number of rows in the Customers table
SELECT COUNT(*)
FROM Customers;
```
Here, the above SQL command counts and returns the number of rows in the `Customers` table.

#### COUNT() With WHERE

We can use `COUNT()` with `WHERE` to count rows that have certain column values:

```sql
-- count of customers who live in the UK
SELECT COUNT(country) AS customers_in_UK
FROM Customers
WHERE country = 'UK';
```

#### COUNT() With DISTINCT
If we need to count the number of unique rows, we can use the `COUNT()` function with the [DISTINCT](https://www.programiz.com/sql/select-distinct) clause. For example,
```sql
-- count the unique countries in Customers table
SELECT COUNT(DISTINCT country)
FROM Customers;
```

#### COUNT() With GROUP BY

The `COUNT()` function can be used with the `GROUP BY` clause to count the rows with similar values. For example,

```sql
-- count the number of customers in each country
SELECT country, COUNT(*) AS customers
FROM Customers
GROUP BY country;
```
Here, the SQL command returns the number of customers in each country.

#### COUNT() With HAVING Clause
We can use `COUNT()` with the `HAVING` clause as follows:
```sql
--count the number of rows by country and return the results for count greater than one
SELECT COUNT(customer_id), country
FROM Customers
GROUP BY country
HAVING COUNT(customer_id) > 1;
```
Here, the SQL command:
1.  counts the number of rows by grouping them by country
2.  returns the result set if their **count** is greater than **1**.

#### COUNT() With NULL Values
1.  `SELECT COUNT(*)` returns the **count of all records** in the result set regardless of NULL values.
2.  `SELECT COUNT(column_name)` returns the **count of records containing non-NULL values** of the specified column.

### SUM / AVG
```sql
--select the sum of amount from Orders table
SELECT SUM(amount) AS total_sales
FROM Orders;
```

```sql
--select the sum of the amount of id 4 from orders
SELECT SUM(amount) AS total_of_cus4
FROM Orders
WHERE customer_id = 4;
```

```sql
-- get average age of customers
SELECT AVG(age) AS average_age
FROM Customers;
```

```sql
--selects the average amount spent by each customer from the Orders table
SELECT customer_id, AVG(amount) AS average_spends
FROM Orders
GROUP BY customer_id;
```

### ORDER BY
The `ORDER BY` clause in SQL is used to sort the result set in ascending or descending order.
```sql
-- orders all rows from Customers in ascending order by country
SELECT *
FROM Customers
ORDER BY country;
```

#### ORDER BY ASC (Ascending Order)
We can use the `ASC` keyword to explicitly sort selected records in **ascending order**. For example,
```sql
-- orders all rows from Customers in ascending order by age 
SELECT *
FROM Customers
ORDER BY age ASC;
```
We use the `DESC` (instead of `ASC`) keyword to sort the selected records in **descending order**. 

#### ORDER BY With Multiple Columns
We can also use `ORDER BY` with multiple columns. For example,
```sql
-- sort all rows from Customers, first by first_name and then by age
SELECT *
FROM Customers
ORDER BY first_name, age;
```
Here, the SQL command selects all the records and then sorts them by `first_name`. If the `first_name` repeats more than once, it sorts those records by `age`.

#### ORDER BY With WHERE
We can also use `ORDER BY` with the `SELECT WHERE` clause. For example,
```sql
-- select last_name and age of customers who don't live in the UK
-- and sort them by last_name in descending order

SELECT last_name, age
FROM Customers
WHERE NOT country = 'UK'
ORDER BY last_name DESC;
```

### GROUP BY
```sql
-- count the number of each country and group the rows by country
SELECT country, COUNT(*) AS number
FROM Customers
GROUP BY country;
```
Here, the SQL command groups the rows by the `country` column, and counts the number of each country (because of the `COUNT()` function).

### LIKE / NOT LIKE
The SQL `LIKE` operator is used with the `WHERE` to get a result set that matches the given string pattern. 
For example,
```sql
-- select customers who live in the UK 
SELECT *
FROM Customers
WHERE country LIKE 'UK';
```

>Note: Although the `LIKE` operator behaves similarly to the `=` operator in this example, they are not the same. The `=` operator is used to check equality whereas `LIKE` operator is used to match string patterns only.

#### SQL LIKE With Wildcards
The SQL `LIKE` query is often used with `wildcards` to match a pattern of string. For example,
```sql
-- SQL LIKE query with wildcard
SELECT *
FROM Customers
WHERE last_name LIKE 'R%';
```

### UNION
```sql
-- select the union of age columns from two tables Teachers and Students 
SELECT age
FROM Teachers
UNION
SELECT age
FROM Students;
```

#### Things to Note While Using UNION

To use `UNION` in SQL, we must always remember,

- The column count in all tables must be the same. For example, both the Teachers and Students tables have three columns.
- The data types of columns must be the same. For example, the age column in Teachers is integer, so is the age in the Students table.
- The columns must be in the same order in each table. For example, the order of columns is **id-name-age** in both Teachers and Students tables.

#### SQL UNION ALL Operator

The `UNION ALL` operator selects fields from two or more tables similar to `UNION`. However, unlike `UNION`, `UNION ALL` _doesn't ignore duplicate fields._

```sql
-- select the union of age from Teachers and Students tables
 
SELECT age
FROM Teachers
UNION ALL
SELECT age
FROM Students;
```

### SUBQUERY
In SQL, it's possible to place a SQL query inside another query. This inner query is known as a _subquery_.
```sql
-- use a subquery to select the first name of customer
-- with the maximum value of customer id
SELECT first_name
FROM Customers
WHERE customer_id= (
SELECT MAX(customer_id)
FROM CUSTOMERS
);
```
-   the subquery selects the maximum id from the _Customers_ table
-   the outer query selects the _first_name_ of the customer with the maximum id (returned by the subquery)

```sql
-- select the customers who have made orders
SELECT customer_id, first_name
FROM Customers 
WHERE customer_id IN (
  SELECT customer_id
  FROM Orders
);
```

### ANY
SQL `ANY` compares a value of the first table with all values of the second table and returns the row if there is a match with any value. Suppose we want to find teachers whose age is similar to any of the student's age. Then, we can use the following query:
```sql
SELECT *
FROM Teachers
WHERE age = ANY (
  SELECT age
  FROM Students
);
```
If there is any match, the corresponding row of the `Teachers` table is selected.

We can use any [comparison operators](https://www.programiz.com/sql/operators#comparision-operators) like `=`, `>`, `<`, etc., with the `ANY` and `ALL` keywords. Let's look at an example where we want teachers whose age is less than any student.
```sql
SELECT * 
FROM Teachers
WHERE age < ANY (
  SELECT age
  FROM Students
);
```

#### Example 3: SQL ALL Operator
For example, if we want to find teachers whose age is greater than all students, we can use
```sql
SELECT * 
FROM Teachers
WHERE age >  ALL (
  SELECT age
  FROM Students
);
```

### CASE
The SQL `CASE` statement is used to check conditions and perform tasks on each row while selecting data.
```sql
-- add a new column 'can_vote' to Customers table
-- insert 'Allowed' into it if customer is older than 17 
SELECT customer_id, first_name,
CASE
  WHEN age >= 18 THEN 'Allowed'
END AS can_vote
FROM Customers;
```
Here, the SQL command checks each row with the given case. The result set contains
-   columns with `customer_id` and `first_name` with their values
-   **Allowed** in the `can_vote` column for rows whose age is greater than or equal to **18**.

#### Multiple CASE
```sql
-- multiple CASE conditions in SQL
SELECT customer_id, first_name,
CASE
    WHEN country = 'USA' THEN 'United States of America'
    WHEN country = 'UK' THEN 'United Kingdom'
END AS country_name
FROM Customers;
```
Here, the result set will contain a field named country_name along with customer_id and first_name.
The value of country_name will be:
-   **United States of America** if the country is **USA**
-   **United Kingdom** if the country is **UK**
-   **Unknown Country** if the country is neither **USA** nor **UK** (because of the `ELSE` clause).

### HAVING
The SQL `HAVING` clause is used if we need to filter the result set based on aggregate functions such as `MIN()` and `MAX()`, `SUM()`, and `AVG()` , and `COUNT()`.
```sql
-- select customers with the same first name based on their age count 
SELECT COUNT(age) AS Count, first_name
FROM Customers
GROUP BY first_name
HAVING COUNT(age) > 1;
```
- counts the `age` of each row and groups them by `first_name`
- returns the result set if the count of `age` is greater than **1** (thus filtering out customers with the same `first_name`)

```sql
-- select the count of customer ids greater than one and their corresponding country 
SELECT COUNT(customer_id), country
FROM Customers
GROUP BY country
HAVING COUNT(customer_id) > 1;
```
Here, the SQL command:
1. counts the number of rows by grouping them by _country_ 
2. returns the result set if their **count** is greater than **1**.

### EXISTS
The SQL `EXISTS` operator tests the existence of any value in a `subquery` i.e. it executes the outer SQL query only if the subquery is not `NULL` (empty result-set).
```sql
-- select customer id and first name of customers
-- whose order amount is less than 12000
SELECT customer_id, first_name
FROM Customers
WHERE EXISTS (
  SELECT order_id
  FROM Orders
  WHERE Orders.customer_id = Customers.customer_id AND amount < 12000
);
```
Here, the SQL query:
- checks for the _order_id_ of customers in the _Orders_ table where amount is less than **12000**
- returns the _customer_id_ and _first_name_ of customers from the _Customers_ table who have made a purchase of less than **12000**

### COALESCE
The SQL `COALESCE` function is used to handle `NULL` values. During the expression evaluation process the `NULL` values are replaced with the user-defined value.
- `SELECT COALESCE(email, 'Email Not Provided') FROM person`

### NULLIF
The `NULLIF()` function returns `NULL` _if two expressions are equal_, otherwise it returns the first expression.

#### Division by Zero
- `SELECT COALESCE(10/NULLIF(0,0), 0)`
	- `NULLIF(0,0)`returns `NULL` as two values are the same
	- `COALESCE` returns `0` as the first expression is `NULL`

### TIMESTAMP and DATE
- `SELECT NOW()`: returns current time
- `SELECT NOW()::DATE`: returns date
- `SELECT NOW()::TIME`: returns time

#### NOW with INTERVAL
- `SELECT NOW() - INTERVAL '1 YEAR'`
- `SELECT NOW() - INTERVAL '10 YEARS'`
- `SELECT NOW() + INTERVAL '10 MONTHS'`
- `SELECT NOW()::DATE + INTERVAL '10 DAYS'`
- `SELECT (NOW() + INTERVAL '10 MONTHS')::DATE`

#### EXTRACT Date
- `SELECT EXTRACT(YEAR FROM NOW())`
- `SELECT EXTRACT(MONTH FROM NOW())`
- `SELECT EXTRACT(DAY FROM NOW())`
- `SELECT EXTRACT(DOW FROM NOW())`: day of week

#### Calculate AGE
- `SELECT AGE(NOW(), date_of_birth) AS age FROM person`

## Basic Operators
### Comparison Operator
- `=`
- `!=` or `<>` : not equal
- `<`
- `>`
- `<=`
- `>=`
### Logical Operators
- All
- AND
- ANY
- BETWEEN: returns 1 if a value is within a range.
- EXISTS 
- IN: returns 1 if a value is in a list of values.
- LIKE: returns 1 if a value matches a pattern
	- Note that we can use regular expression`REGEXP`
- NOT: reverses the value of other operators such as NOT EXISTS, NOT IN, NOT BETWEEN, etc.
- OR

## Basic Arithmetic Operation
- `SELECT 10+2;`
- `SELECT 10%2;`: modulo
- `SELECT 10^2;`: power
- `SELECT 5!;`: factorial
- `SELECT price, price*0.10 FROM car;`
	- `SELECT price, ROUND(price*0.10) FROM car;`
	- `SELECT price AS original_price, ROUND(price*0.10) AS dicount FROM car;`
 
## JOIN
The SQL `JOIN` joins two tables based on a common column and selects records that have matching values in these columns.
```sql
-- join Customers and Orders tables based on
-- customer_id of Customers and customer column of Orders
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer;
```

#### JOIN with Aliases
```sql
-- use alias C for Customers table
-- use alias O for Orders table
SELECT C.customer_id AS cid, C.first_name AS name, O.amount
FROM Customers AS C
JOIN Orders AS O
ON C.customer_id = O.customer;
```

### INNER JOIN
This is functionally equivalent to `JOIN`.

### Left Join
The SQL `LEFT JOIN` joins two tables based on a common column. It selects records that have matching values in these columns and the remaining rows from the left table.
```sql
-- left join the Customers and Orders tables
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer;
```
Here, the SQL command selects the `customer_id` and `first_name` columns (from the `Customers` table) and the `amount` column (from the `Orders` table).

The result set will contain those rows where there is a match between `customer_id` (of the `Customers` table) and `customer` (of the `Orders` table), _along with all the remaining rows_ from the `Customers` table.

#### LEFT JOIN with WHERE
```sql
SELECT Customers.customer_id, Customers.first_name, Orders.amount
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer
WHERE Orders.amount >= 500;
```

## CREATE DATABASE
The `CREATE DATABASE` statement is the SQL command used to create databases. The syntax of the SQL `CREATE DATABASE` statement is:
```sql
CREATE DATABASE DB_NAME;
```

#### CREATE DATABASE IF NOT EXISTS

If a database already exists, SQL will throw an error while creating another database of the same name. In such situations, we can use the `CREATE DATABASE IF NOT EXISTS` statement to create a database only if there is no existing database with the same name. For example,
```sql
CREATE DATABASE IF NOT EXISTS my_db;
```
Here, the SQL command creates a database named `my_db` only if there is no existing database with the same name.

#### List All Databases
```sql
SHOW DATABASES;
```

#### Switch Databases
We often have to work with multiple databases. To switch between available databases, we can run the following statement.
```sql
USE my_db;
```
This code selects the `my_db` database, and all SQL operations will be performed inside this database.

### CREATE TABLE
A database table is used to store records (data). To create a database table, we use the SQL `CREATE TABLE` statement.

### DROP DATABASE & TABLE
In SQL, `DROP DATABASE` is used to delete a database from our Database Management System.
```sql
DROP DATABASE my_database;
```
Here, the SQL command will delete a database named my_database. Also, you need **admin** or **DROP** permission to run this command.

The syntax of the SQL `DROP TABLE` statement is:
```sql
DROP TABLE table_name;
```

#### DROP TABLE IF EXISTS
If a table does not exist, dropping it will throw an error. To fix this issue, we can add the optional `IF EXISTS` command while dropping a table. For example,
```sql
-- delete Orders table if it exists
DROP TABLE IF EXISTS Orders;
```

### ALTER TABLE 
In SQL, the `ALTER TABLE` command is used to modify the structure of an existing table like adding, deleting, renaming columns, etc.
```sql
-- add phone column to Customers table
ALTER TABLE Customers
ADD phone varchar(10);
```

### ADD

### RENAME
```sql
-- rename column customer_id to c_id
ALTER TABLE Customers
RENAME COLUMN customer_id TO c_id;
```

### MODIFY

### DELETE
- `DELETE FROM person WHERE id==100`

## BACKUP DATABASE

In SQL, the `BACKUP DATABASE` statement is used to create database backups.
```sql
-- backup database to the given path
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak';
```
Here, the SQL command creates a backup file of the my_db database inside **C** drive, named `my_db_backup.bak`.

### Full Backup
```sql
BACKUP DATABASE database_name
TO medium = 'path/file_name';
```
- `database_name` is the name of the database to be backed up
- `medium` refers to the storage medium such as disk, tape or url
- `path` refers to the folder where the backup file should be stored
- `file_name` is the name given to the backup file

For example,
```sql 
-- backup database to the given path
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak';
```

### Differential Backup
In SQL, you can also backup only the new changes compared to the last full backup by using the `WITH DIFFERENTIAL` command. For example,
```sql
-- backup the changes made to the database
BACKUP DATABASE my_db
TO DISK = 'C:\my_db_backup.bak'
WITH DIFFERENTIAL;
```

### Transaction Log Backup
A transaction log backup _captures all the changes made to the database_ since the last transaction log backup or the creation of the database. It allows you to create a point-in-time backup of your database and provides a way to recover the database to a specific point in time in case of a failure.
```sql
-- backup database log to the given path
BACKUP LOG my_db
TO DISK = 'C:\my_db_backup.bak';
```

### Restore Database From Backup
To restore a backup file to a database management system, we can use the `RESTORE DATABASE` command. For example,
```sql
-- restore database from given path
RESTORE DATABASE my_db
FROM DISK = 'C:\my_db_backup.bak';
```


## UPDATE, INSERT, DELETE
### INSERT INTO
In SQL, the `INSERT INTO` statement is used to insert new rows in a database table.
```sql
INSERT INTO Customers(customer_id, first_name, last_name, age, country)
VALUES
(7, 'Ron', 'Weasley', 31, 'UK');
```

#### Skip Auto Incremented Fields While Inserting a Row
In a database table, the **ID** field is usually unique and auto incremented. In such cases, we can omit the value for that column during row insertion. For example,
```sql
-- insert a row to Customers table
-- skip auto incremented customer_id column
INSERT INTO Customers(first_name, last_name, age, country)
VALUES
('James', 'Bond', 48, 'USA');
```

#### Insert Multiple Rows at Once in SQL
It's also possible to insert multiple rows to a database table at once. For example,
```sql
INSERT INTO Customers(first_name, last_name, age, country)
VALUES
('Harry', 'Potter', 31, 'USA'),
('Chris', 'Hemsworth', 43, 'USA'),
('Tom', 'Holland', 26, 'UK');
```

### UPDATE
```sql
-- update a single value in the given row
UPDATE Customers
SET age = 21
WHERE customer_id = 1;
```
Here, the SQL command changes the value of the `age` column to **21** if customer_id is equal to **1**.

#### Update multiple values
```sql
-- update multiple values in the given row
UPDATE Customers
SET first_name = 'Johnny', last_name = 'Depp'
WHERE customer_id = 1;
```

#### Update all rows
```sql
-- update country info of all rows 
UPDATE Customers
SET country = 'NP';
```

### SELECT INTO

In SQL, the `SELECT INTO` statement is used to copy data from one table to another.
```sql
-- copy all the contents of a table to a new table
SELECT *
INTO CustomersCopy
FROM Customers;
```
Here, the SQL command copies all data from the `Customers` table to the new `CustomersCopy` table.

#### Copy Records Matching a Condition
We can use the `WHERE` clause with `SELECT INTO` to copy those rows that match the specified condition. For example,
```sql
-- copy rows where country is USA
SELECT customer_id, age
INTO USACustomersAge
FROM Customers
WHERE country = 'USA';
```
- creates the `USACustomersAge` table with `customer_id` and `age` columns
- copies rows from the `Customers` table if the value of the country column is **USA**

#### Copy to Another Database
By default, `SELECT INTO` creates a new table in the current database. If we want to copy data to a table in a different database, we can do that by using the `IN` clause. For example,
```sql
-- copy contents of a table to another database
SELECT *
INTO CustomersCopy
IN another_db.mdb
FROM Customers;
```
Here, the SQL command copies the `Customers` table to the `CustomersCopy` table in the another_db.mdb database.
>**Note:** The user must have **WRITE** privilege to copy data to a table in a different database.

#### Copy From Two Tables to One
We can also copy records from two different tables to a new table using the `JOIN` clause with `SELECT INTO`. For example,
```sql
-- copy rows from Customers and Orders tables
SELECT Customers.customer_id, Customers.first_name, Orders.amount
INTO CustomerOrders
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;
```

Here, the SQL command copies `customer_id` and `first_name` from the `Customers` table and amount from the `Orders` table to a new table `CustomerOrders`.

#### Copy Table Schema Only
We can also use the `SELECT INTO` statement to create a new table with the given structure (without copying the data). For that, we use the `WHERE` clause with a condition that returns `false`.
```sql
-- copy table structure only
SELECT *
INTO NewCustomers
FROM Customers
WHERE false;
```
Here, the SQL command creates an empty table named NewCustomers with the same structure as the Customers table.

### INSERT INTO
The SQL `INSERT INTO SELECT` statement is used to copy records from one table to another existing table. The syntax of the SQL `INSERT INTO SELECT` statement is:
```sql
INSERT INTO destination_table (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM source_table;
```
Here,
-   `destination_table` is the name of the table where the data is to be inserted
-   `column1, column2, column3, ...` are the names of the columns to be copied
-   `source_table` is the name of the table from where you want to select the data.

```sql
-- copy rows that satisfy the condition
INSERT INTO OldCustomers
SELECT *
FROM Customers
WHERE country = 'USA';
```

### DELETE
In SQL, the `DELETE` clause is used to delete row(s) from a database table.
```sql
DELETE FROM Customers
WHERE customer_id = 4;
```

#### Delte All Rows
```sql
DELETE FROM Customers;
```

## CONSTRAINTS 
In a database table, we can add rules to a column known as **constraints**. These rules control the data that can be stored in a column.

### NOT NULL 
- values cannot be null
### UNIQUE 
- values cannot match any older value
- We can add a constraint to the email column to make it unique: 
- `ALTER TABLE person ADD CONSTRAINT UNIQUE (email);`
	- Set the constraint as `unique_email_address` `ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE (email);`
	- Drop the constraint`ALTER TABLE person DROP CONSTRAINT unque_email_address;
### PRIMARY KEY 
- used to uniquely identify a row
- Discard primiary key:
	- `ALTER TABLE person DROP CONSTRAINT person_pkey;`
- Add primiary key:
	- `ALTER TABLE person ADD PRIMARY KEY (id);`
	- Use a `id` column as a primary key
 
### FOREIGN KEY 
- references a row in another table

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables. A `FOREIGN KEY` is a field (or collection of fields) in one table, that refers to the `PRIMARY KEY` in another table. The table with the foreign key is called the _child table_, and the table with the primary key is called the referenced or _parent table_.

Let's say we have two tables, Person and Order.  Notice that the "PersonID" column in the "Orders" table points to the "PersonID" column in the "Persons" table. The "PersonID" column in the "Persons" table is the `PRIMARY KEY` in the "Persons" table. The "PersonID" column in the "Orders" table is a `FOREIGN KEY` in the "Orders" table. The `FOREIGN KEY` constraint _prevents invalid data from being inserted into the foreign key column, because it has to be one of the values contained in the parent table_.

```sql
CREATE TABLE customers(    
customer_id INT GENERATED ALWAYS AS IDENTITY,    
customer_name VARCHAR(255) NOT NULL,    
PRIMARY KEY(customer_id) );  

CREATE TABLE contacts(    
contact_id INT GENERATED ALWAYS AS IDENTITY,    
customer_id INT,    
contact_name VARCHAR(255) NOT NULL,    
phone VARCHAR(15),    
email VARCHAR(100),    
PRIMARY KEY(contact_id),    
CONSTRAINT fk_customer       
FOREIGN KEY(customer_id)  	  
REFERENCES customers(customer_id) );
```

In this example, the `customers` table is the **parent table** and the `contacts` table is the **child table**. Each customer has zero or many contacts and each contact belongs to zero or one customer. The `customer_id` column in the `contacts` table is the foreign key column that references the primary key column with the same name in the `customers` table. 

### CHECK 
- validates condition for new value
- `ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender=='Female' OR gender=='Male');`

### DEFAULT 
- set default value if not passed

### CREATE INDEX 
- used to speedup the read process

## Duplicate Key Errors
```sql
INSERT INTO Customers(first_name, last_name, age, country) VALUES ('James', 'Bond', 48, 'USA')
ON CONFLICT (id) DO NOTHING;
```
- This command inserts values if there is no duplicate in `id`.
- If there is a duplicate, then it does nothing. 

If we wanna do something else than `DO NOTHING`, then
```sql
INSERT INTO Customers(first_name, last_name, age, country) VALUES ('James', 'Bond', 48, 'USA')
ON CONFLICT (id) DO UPDATE SET EMAIL = EXCLUDED.last_name;
```
- `EXCLUDED.last_name`: the last name of the one which is about to be inserted as above (Bond)

## Exporting QUERY Results to CSV
- `\copy (<SQL Command>) TO '<path>' DELIMITER ',' CSV HEADER`:
    - `HEADER`: to include HEADER (column header) 




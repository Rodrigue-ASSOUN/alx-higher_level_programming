### Creating a New MySQL User:
To create a new MySQL user, you typically use the `CREATE USER` command followed by the username and identified by a password. Here's a basic syntax:
```sql
CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';
```

### Managing Privileges:
To grant privileges to a user, you use the `GRANT` statement. For example, to grant all privileges on a specific database to a user:
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'hostname';
```

### PRIMARY KEY:
A PRIMARY KEY is a unique identifier for each record in a table. It ensures that each row in a table is uniquely identified. For example:
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

### FOREIGN KEY:
A FOREIGN KEY is a field or a set of fields in one table that refers to the PRIMARY KEY or UNIQUE KEY in another table. It establishes a relationship between two tables. For example:
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### NOT NULL and UNIQUE Constraints:
- `NOT NULL` constraint ensures that a column cannot have a NULL value.
- `UNIQUE` constraint ensures that all values in a column are different.

Example:
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE
);
```

### Retrieving Data from Multiple Tables:
To retrieve data from multiple tables, you use SQL JOINs. For example, to get data from two tables, `orders` and `customers`:
```sql
SELECT orders.order_id, orders.order_date, customers.customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;
```

### Subqueries:
A subquery is a query nested within another query. It can be used to return data that will be used by the main query. For example:
```sql
SELECT name, age
FROM students
WHERE age > (SELECT AVG(age) FROM students);
```

### JOIN and UNION:
- **JOIN:** Combines rows from two or more tables based on a related column.
- **UNION:** Combines the result sets of two or more SELECT statements into a single result set.

Example:
```sql
-- JOIN
SELECT orders.order_id, orders.order_date, customers.customer_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;

-- UNION
SELECT city FROM customers
UNION
SELECT city FROM suppliers;
```

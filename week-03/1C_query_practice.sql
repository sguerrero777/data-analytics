-- ============================================================
-- Excercise1.C: More Practice With Queries
-- Sharleen Guerrero
-- ============================================================

USE northwind;
-- Question 1: Write a query to list the product id, product name, and unit price of every product. This time, display them in ascending order by price.
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;
-- Returns 77 records

-- Question 2: What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price. 
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;
-- Returns 10 records

-- Question 3: What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price. If two or more have the same price, list those in ascending order by product name. 
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC; 
-- Returns 10 records

-- Question 4: Write a query against the orders table that displays the total number of distinct customers who have placed orders, based on customer ID. Use an alias to label the  count calculation as CustomerCount. 
SELECT COUNT(DISTINCT CustomerID) AS 'CustomerCount'
FROM orders;
-- Returns Customer Count:89

-- Question 5: Write a query against the orders table that displays the total number of distinct customers who have placed orders, by customer ID, for each country where orders have been shipped. Again, use an alias to label the count as CustomerCount. Order the list by the CustomerCount, largest to smallest. 
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS 'CustomerCount'
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;
-- Returns 21 rows

-- Question 6: What are the products that we carry where we have less than 25 units on hand, but 1 or more units of them are on order? Write a query that orders them by quantity on order (high to low), then by product name. 
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25 AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName;
-- Returns 17 records

-- Question 7: Write a query to list each of the job titles in employees, along with a count of how many employees hold each job title.
SELECT Title, COUNT(*) AS 'EmployeeCount'
FROM employees
GROUP BY Title;
-- Returns counts: Sales Reps (6) and Inside Sales Coordinator, Sales Manager and Vice President of Sales (each 1)
-- Nine employees total.

-- Question 8: What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title.
SELECT EmployeeID, CONCAT(FirstName, ' ', LastName) AS 'Employee Name', Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;
-- Returns 4 records
-- CONCAT was used to combine two columns into one column with its lias as EmployeeName 
-- Employees with a monthly salary between $2000 and $2500 are:
-- Laura Callahan, Michael Suyama, Anne Dodsworth, Andrew Fuller
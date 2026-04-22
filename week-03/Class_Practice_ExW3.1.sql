-- Question 1

USE northwind;

SELECT CategoryID, CategoryName, Description
FROM Categories;

-- Question 2
SELECT ProductID, ProductName, QuantityPerUnit
FROM products
WHERE QuantityPerUnit LIKE '%box%';

-- Question 3
SELECT ProductID, ProductName, Discontinued
FROM products
WHERE Discontinued = 1;

-- Question 4
SELECT EmployeeID, CONCAT(FirstName, ' ', LastName) AS 'FullName', Title
FROM employees;

-- Question 5


-- Question 6

-- Question 7






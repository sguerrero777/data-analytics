-- ============================================================
-- Excercise3.A: Aggregate Functions and Grouping
-- Sharleen Guerrero 
-- ============================================================

USE northwind; 

-- Question 1: Write a query to find the price of the cheapest item that Northwind sells. Then write a second query to find the name of the product that has that price. 
SELECT MIN(UnitPrice) AS 'CheapestItem'
FROM products;
-- Cheapest Item: 2,5000

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- Cheapest Item is Geitost

-- Question 2: Write a query to find the average price of all items that Northwind sells. 
SELECT AVG(UnitPrice) AS AveragePrice
FROM products; -- $28.86636364

-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help using the ROUND function to round the average price to the nearest cent.) 
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM products; -- $28.87 

-- Question 3: Write a query to find the price of the most expensive item that Northwind sells. Then write a second query to find the name of the product with that price, plus the name of the supplier for that product. 
SELECT MAX(UnitPrice) AS 'MostExpensiveItem'
FROM products;
-- Most Expensive Item: 263,5000

SELECT p.ProductName, p.UnitPrice, s.CompanyName AS 'Supplier'
FROM products p
INNER JOIN suppliers s
	ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM products);
-- Subquery used for this problem
-- Most expensive prodcut is Cte de Blaye from Aux joyeuz ecclsiastiques

-- Question 4: Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries). 
SELECT ROUND(SUM(Salary), 2) AS MonthlySalary
FROM employees; 
-- Monthly Salary: $20362.93

-- Question 5: Write a query to identify the highest salary and the lowest salary amounts which any employee makes. (Just the amounts, not the specific employees!) 
SELECT MAX(Salary) AS 'Highest Salary',
	   MIN(Salary) AS 'Lowest Salary'
FROM employees;
-- Highest Salary: $3119.15
-- Lowest Salary: $1,744.21

-- Question 6: Write a query to find the name and supplier ID of each supplier and the number of items they supply.
SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS 'ItemCount'
FROM suppliers s
INNER JOIN products p
	ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY ItemCount DESC;
-- Returns 29 rows

-- Question 7: Write a query to find the list of all category names and the average price for items in each category. 
SELECT c.CategoryID, c.CategoryName, ROUND(AVG(p.UnitPrice), 2) AS 'AvgPrice'
FROM categories c
INNER JOIN products p
	ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName
ORDER BY AvgPrice;
-- Returns 8 rows

-- Question 8: Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of each supplier and the number of items they supply. 
SELECT s.CompanyName AS Supplier, COUNT(p.ProductID) AS 'ItemsSupplied'
FROM suppliers s
INNER JOIN products p
	ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING ItemsSupplied >= 5
ORDER BY ItemsSupplied;
-- Returns 2 records
-- Pavlova and Plutzer

-- Question 9: Write a query to list products currently in inventory by the product id, product name, and inventory value (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.
SELECT ProductID, ProductName, ROUND(UnitPrice * UnitsInStock, 2) AS 'InventoryValue'
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;
-- Returns 72 records
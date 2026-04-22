-- Sharleen B. Guerrero
-- April 20, 202
-- SHOW DATABASES;

USE northwind;
SHOW TABLES;
SELECT table_name
FROM information_schema.tables
WHERE table_schema - 'northwind'
	AND table_type - 'BASE TABLE';

-- Example 1: Retrieving specific columns from product table
SELECT ProductName, UnitPrice FROM products; 

-- Example 2: Retrieving all columns from product table
SELECT * FROM products; -- Retrieves 77 records

-- Example 3: Using Aliases
-- AS renames a column in the result set and only affects the output name.
-- Rename columns ProductName, UnitPrice, and UnitsInStock as Product, Price(USD), and Stock for clarity.
SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock AS 'Stock'
FROM products;

-- Example 4: Using WHERE clause
-- WHERE sets a condition to filter results
-- Retrieve all company names, cities, and country from Germany
SELECT CompanyName, City, Country 
FROM customers
WHERE Country = 'Germany';

-- Example 5: WHERE CLAUSE continued
-- Retrieve all ProductName and UnitPrice from the Product table, where UnitPrice is greater than 50. 
-- Hint: Single quotes to enclose is only for Strings (words)
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice > 50;

-- Example 6: Using SELECT...WHERE Statements
-- Retrieve all the OrderID, CustomerID, ShipCountry, and Freight from the Orders table for all orders shipped to France.
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM orders
WHERE ShipCountry = 'France';

-- Example 7: Retrieve all products whose current stock is below the reorder threshold.
SELECT ProductName, UnitsInStock, ReorderLevel
FROM products
WHERE UnitsInStock < ReorderLevel;

-- Example 8: Workding with Conditional Logic
-- Retrieve all OrderID and Freight for Freight orders greater or equal to 100
SELECT OrderID, Freight
FROM orders
WHERE Freight >= 100;

-- Example 9: Logical Operators 
-- These operators let you combine multiple conditions in a where clause
-- Retrieve all products, unit price, and units in stock for products with unit price greater than 20 and units in stock greater than 50
SELECT ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitPrice > 20 AND UnitsInStock > 50; 

-- Example 10: Retrieve all company amd country names from either UK or Ireland
SELECT CompanyName, Country
FROM Customers
WHERE Country = 'UK' OR 'Ireland';

-- Example 11: Retrieve all Products, CategoryID and UnitPrice for products with a CategoryID of 1 or 2 and a UnitPrice less than 20
SELECT ProductName, CategoryID, UnitPrice
FROM products
WHERE (CategoryID = 1 OR CategoryID = 2) 
AND UnitPrice < 20;

-- Example 12: Using the NOT Operator
-- Used to negate a condition, flips true to false and vice versa
-- Retrieve all company names, and country names other than the USA
SELECT CompanyName, Country
FROM Customers
WHERE NOT Country = 'USA';
-- WHERE Country != 'USA'; is also good

-- Example 13: Retrieve all products that are currently active. Not discontinued.
SELECT ProductName
FROM products
WHERE Discontinued != 1;

-- Example 14: Retrieve company names from the following countries France, Germany, and Spain
SELECT CompanyName, Country
FROM Customers
WHERE Country IN ('France', 'Germany', 'Spain');

-- Example 15: Retrieve Product Names and SupplierID from suppliers other than those with SupplierID 1,2, or 3
SELECT ProductName, SupplierID
FROM products 
WHERE SupplierID NOT IN ('1', '2', '3');

-- Example 16: Using BETWEEN Operator
-- Selects the value within specific range
-- Retrieves the ProductName and UnitPrice for all products with a unit price between 10 and 20
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice BETWEEN 10 AND 20;

-- Example 17: Testing for Null
-- Retrieve the OrderID, CustomerID, and Ship Region for orders where the ShipRegion field has not been filled in.
SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS NULL;

-- Example 18: Testing Null continued
-- Retrieves employees first name, last name, and regions that are filled in
SELECT FirstName, LastName, Region
FROM employees
WHERE Region IS NOT NULL;

-- Example 19: Using the LIKE Operator
-- Often used with wildcards % and _, _ for exactly on character and % for zero or multiple characters
-- Retrieve all company names that start with A
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';

-- Example 24: Using WHERE Condition with Dates
-- Define Column as DATE to only store DATE without the time, Northwind database need cleaning
-- Retrieves OrderID, CustomerID, OrderDate for all orders with a shipped date of '1997-01-01'
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate = '1997-01-01';

-- Example 26: Retrieves all orders placed in June 1977 using YEAR() AND MONTH() Functions
SELECT OrderID, OrderDate
FROM orders
WHERE YEAR(OrderDate) = 1997 AND MONTH(OrderDate) = 6;

-- Example 27: Using ASC, DESC
-- Retrieve all product names and price in descending order
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC;

-- Example 28:
-- Retrieves company names alphabetically by country then Name
-- Customers are first grouped by Country alphabetically. Within each country, they are further sorted by CompanyName
SELECT CompanyName, Country, City
FROM customers
ORDER BY Country ASC, CompanyName ASC;

-- Example 32: Sampling Records with LIMIT
-- Retrieves the top 5 most expensive products
SELECT ProductName, UnitPrice
FROM products 
Order By UnitPrice DESC -- Orders it by most expensive
LIMIT 5;

-- Example 30: Using LIMIT OFFSET
-- Retrieves products and prices for rows 6 through 10 and skips the first 5 rows;
SELECT ProductName, UnitPrice
FROM products 
Order By UnitPrice DESC -- Orders it by most expensive
LIMIT 5 OFFSET 5;

-- Example 31: Using DISTINCT
-- Retrieves only unique/non-duplicate values
-- Returns each unique pairing of Country and City.
-- If two customers share the same city, that city apppears only once
SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country, City;

-- Example 33: Concatenation
-- Returns Full Name from First and Last
SELECT CONCAT(FirstName, ' ', LastName) AS 'Full Name',
	Title
FROM Employees;

-- Example 36: Adding Calculations to Results
-- Returns prodcuts with original price and a 10% discount
-- This combines using an Alias for new and old totals
SELECT ProductName, UnitPrice AS 'Original Price',
UnitPrice * 0.90 AS '10% Discount Price'
FROM products
ORDER BY ProductName ASC;





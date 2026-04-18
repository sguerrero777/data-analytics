/*
a) The name of the table that holds the items Northwind sells is the products table.
b) The name of the table that holds the types/categories of the items Northwind sells is the categories table.
*/ 

USE Northwind; 

SELECT * FROM employees;
--  5a) The employee whose name makes it look like she's a bird is Margaret Peacock (Sales Representative).

SELECT * FROM products; -- 6a) Returns 77 records
-- To retrieve 10 rows only using the toolbar, change the default dropdown from "Limit to 1000" to "Limit to 10". This ensures only 10 records are retrieved.
-- 6b) BONUS:
-- Without using the toolbar, I can write the query to only retrieve a certain amount of records by using the LIMIT clause:
-- I used W3 Schools for my conclusion: https://www.w3schools.com/mysql/mysql_limit.asp

SELECT * FROM categories;
-- 7c) The category ID for seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 50;
-- Result was exported and pushed to GitHub. 


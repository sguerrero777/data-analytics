USE northwind;

--  Question 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice 
FROM products; 
-- Returns 77 records
  
-- Question 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductName, UnitPrice 
FROM products
WHERE UnitPrice <= 7.50; 
-- Returns 5 records

-- Question 3: What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
SELECT ProductName, UnitsInStock, UnitsOnOrder 
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;
-- Returns 1 record

-- Question 4: Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these  questions, ending with a query that creates a list of all the seafood items we carry.
-- The products table identifies the type of each item sold with the CategoryID.
-- To find a list of all categories, retrieve it from the categories table using the CategoryID and CategoryName.
SELECT CategoryID, CategoryName
FROM categories; -- This finds the list of all categories, CategoryID for Seafood is 8.

-- To list of all seafood items we carry, use the product table now that we know the CategoryID for Seafood is 8.
SELECT CategoryID, ProductName
FROM products
WHERE CategoryID = 8;
-- Returns 8 records

-- Question 5: Examine the products table again. How do you know what supplier each product  comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.
-- I know what supplier each product comes from using the SupplierID, and I can find info on suppliers in the suppliers table.
-- Finding the identifier for "Tokyo Trader" supplier
SELECT SupplierID, CompanyName
FROM suppliers
WHERE CompanyName = 'Tokyo Traders'; -- SupplierID for "Tokyo Traders" is 4.

-- Finding all products from this supplier.
SELECT SupplierID, ProductName
FROM products
WHERE SupplierID = 4;
-- Returns 3 records

-- Question 6: How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question.
-- To find how many employees work at northwind
SELECT EmployeeID
FROM employees;
-- Returns 9 records, so 9 employees work at northwind.

SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%Manager%';
-- Steven Buchanan is the Sales Manager.

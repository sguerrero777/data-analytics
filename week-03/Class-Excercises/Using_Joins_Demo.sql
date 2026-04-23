-- Sharleen B. Guerrero
-- April 22, 2026
-- USING JOINS

USE northwind;

-- Example 1: Return OrderID, Customer, and OrderDate. Limit to 5 records
SELECT o.OrderID,
	   c.CompanyName AS 'Customer',
       o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC
LIMIT 5;

-- Example 2: Return Order ID, CompanyName and OrderDate with a Limit of 5. Orders Joined to Customers.
-- USING only works when the joing column has the same names in both tables. If columns names differ, use ON instead.
SELECT OrderID, CompanyName, OrderDate
FROM orders
JOIN Customers USING (CustomerID)
ORDER BY OrderDate
LIMIT 5; 

-- Example 3: Return ProductName, CategoryName, and UnitPrice with LIMIT of 6. Products with their Category Name
SELECT p.ProductName,
	   c.CategoryName,
       p.UnitPrice
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- USING also works here
SELECT p.ProductName,
	   c.CategoryName,
       p.UnitPrice
FROM Products p
INNER JOIN Categories c USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- Example 4: OUTER JOINS
-- Return all Customers including those with No Orders
-- Customers with zero orders will show 0 in Order Count
SELECT c.CompanyName,
	   COUNT(o.OrderID) AS 'Order Count'
FROM Customers c
LEFT JOIN Orders O ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY 'Order Count' ASC
LIMIT 5;
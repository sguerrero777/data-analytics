-- ============================================================
-- Using Aggregate Functions Demo
-- Sharleen Guerrero
-- April 23, 2026
-- ============================================================

USE northwind;

-- Example 1: Total Number of Orders
-- Find out how many orders are recorded in the Orders table in total
SELECT COUNT(DISTINCT OrderID) AS 'OrderCount'
FROM orders;

-- Example 2: Total Freight Charged
-- Calculate the total freight charges calcualted across all orders.
SELECT 
    SUM(Freight) AS 'TotalFreight',
    AVG(Freight) AS 'AverageFreight',
    MIN(Freight) AS 'MinimumFreight',
    MAX(Freight) AS 'MaximumFreight'
FROM Orders;

-- Example 3
-- Find out how many differenct countries northwind customers come from
SELECT COUNT(DISTINCT Country) AS total_countries
FROM Customers;
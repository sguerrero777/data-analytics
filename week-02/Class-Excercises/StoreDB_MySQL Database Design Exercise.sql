-- ============================================================
-- Excercise: MySQL Database Design with Relationships
-- Tables: Customer and Product (1:Many Relationship)
-- ============================================================

-- Sharleen B. Guerrero

-- ============================================================
-- STEP 1: CREATE DATABASE
-- ============================================================

CREATE DATABASE IF NOT EXISTS StoreDB;
USE StoreDB;

-- ============================================================
-- STEP 2: ADD TABLES
-- ============================================================

-- Create the Customer table (the "one" side of the relationship)
CREATE TABLE Customer (
	CustomerID   INT	      NOT NULL AUTO_INCREMENT,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerZip  CHAR(5)      NOT NULL,
    PRIMARY KEY (CustomerID)
);

-- Create the Product table (the "many" side of the relationship)
CREATE TABLE Product (
	ProductID   INT           NOT NULL AUTO_INCREMENT,
    ProductName VARCHAR(100)  NOT NULL,
    Quantity 	INT           NOT NULL DEFAULT 0,
    UnitPrice   DECIMAL(10,2) NOT NULL,
    TotalPrice  DECIMAL(10,2) NOT NULL,
    CustomerID  INT           NOT NULL,
    PRIMARY KEY (ProductID), 
    -- ============================================================
    -- STEP 3: ESTABLISH RELATIONSHIP
    -- Foreign key linking Product to Customer (1:Many)
    -- One customer can have many products
    -- ============================================================
    CONSTRAINT fk_customer
    FOREIGN KEY (CustomerID)
    REFERENCES Customer(CustomerID)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);

-- ============================================================
-- STEP 4: ADD INITIAL RECORDS
-- ============================================================

-- Insert Customer Records
INSERT INTO Customer (CustomerName, CustomerZip) VALUES
	('Alice Johnson', '10001'),
    ('Bob Martinez',  '90210'),
    ('Carol Thompson','60601'),
    ('David Lee',     '77001'),
    ('Eva Williams',  '30301');
    
-- Insert Product records (each linked to a CustomerID)
-- TotalPrice = Quantity * UnitPrice (calculated manually)
INSERT INTO Product (ProductName, Quantity, UnitPrice, TotalPrice, CustomerID) VALUES
	('Wireless Mouse',   		    2,   29.99, 59.98, 1),
    ('USB-C Hub',        		    1,   49.99, 49.99, 1),
    ('Laptop Stand',     		    1,   39.95, 39.95, 2),
    ('Mechanical Keyboard', 	    1, 109.00, 109.00, 2),
    ('Monitor', 				    2, 299.99, 599.98, 3),
    ('Webcam HD', 				    1,   74.50, 74.50, 3),
    ('Desk Lamp', 				    3,   22.00, 66.00, 4),
    ('Noise Cancelling Headphones', 1, 199.99, 199.99, 5);
    
-- ============================================================
-- STEP 5: ADD ADDITIONAL RECORDS (Updates / New Data)
-- ============================================================

-- Add two new customers
INSERT INTO Customer (CustomerName, CustomerZip) VALUES
	('Frank Garcia', '85001'),
    ('Grace Kim',    '98101');

-- Add new products for the new customers
INSERT INTO Product (ProductName, Quantity, UnitPrice, TotalPrice, CustomerID) VALUES
	('Smart Speaker',   		      1,   99.99, 99.99, 6),
    ('Cable Oranizer',        		  4,    9.99, 39.96, 6),
    ('Drawing Tablet',     		      1, 249.00, 249.00, 7),
    ('Screen Claner Kit', 	          2,   12.50, 25.00, 7);
    
-- Add additional products to existing customers
INSERT INTO Product (ProductName, Quantity, UnitPrice, TotalPrice, CustomerID) VALUES
('Ergonomic Chair',   		      1,   350.00, 350.00, 1),
('Blue Light Glasses',      	  1,     25.00, 25.00, 3);
    
-- ============================================================
-- VERIFICATION QUERIES
-- ============================================================

-- View all customers
SELECT * FROM Customer;

-- View all products with computed TotalPrice
SELECT * FROM Product;

-- View products joined with customer names
SELECT
	c.CustomerID,
    c.CustomerName,
    c.CustomerZip,
    p.ProductID,
    p.ProductName,
    p.Quantity,
    p.UnitPrice,
    p.TotalPrice
FROM Customer c
JOIN Product p ON c.CustomerID = p.CustomerID
ORDER BY c.CustomerID, p.ProductID;

SELECT c.CustomerID, c.CustomerName, COUNT(p.ProductID) AS ProductCount
FROM Customer c
JOIN Product p ON c.CustomerID = p.CustomerID
GROUP BY c.CustomerID, c.CustomerName
HAVING COUNT(p.ProductID) > 1;
 
/*
Discussion Questions
*/

-- 1. Why is CustomerID defined as AUTO_INCREMENT? What benefit does this provide?
-- Customer ID is defined as AUTO_INCREMENT to automatically generate a unique identifier everytime a new customer is added. This gives the benefit of reducing the need to manually create a new ID for new records, which prevents duplicate IDs from being created.

-- 2. What happens to Product records if a Customer is deleted? How does ON DELETE CASCADE affect this?
-- If a Customer is deleted, the Product record gets deleted entirely automatically. ON DELETE CASCADE affects this becasue it ensures that any child records connected to the deleted parent data is also deleted, keeping data consistent.

-- 3. Why is TotalPrice defined as a GENERATED column instead of being manually entered?
-- TotalPrice (Quantity x UnitPrice) would be better defined as a GENERATED column because it can automatically make calcuations. Manual input can lead to human error and data inconstencies.

-- 4. How would you modify the schema if a product could belong to multiple customers?
-- If a product could belong to multiple customers, this would create a many-to-many relationship in the schema and would require a bridge table to resolve it. I would create a junction table called Orders with field OrderID as the primary key and both CustomerID and ProductID as foreign keys linking the Customer and Product table together. 

-- 5. Write a query that shows only customers who have more than one product ordered.
-- SELECT c.CustomerID, c.CustomerName, COUNT(p.ProductID) AS ProductCount
-- FROM Customer c
-- JOIN Product p ON c.CustomerID = p.CustomerID
-- GROUP BY c.CustomerID, c.CustomerName
-- HAVING COUNT(p.ProductID) > 1;
-- I used W3 Schools to write this, since I was unfamiliar with writing aggregate queries: https://www.w3schools.com/sql/sql_having.asp
--  SELECT: What to show
-- FROM/JOIN: Which tables to connect
-- GROUP BY: Group by customer
-- HAVING: Only shows customers with more than 1 product.
    
    
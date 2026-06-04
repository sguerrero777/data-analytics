# Exercise 2A | Northwind Database Review
**Name**: Sharleen Guerrero
**Date**: June 3, 2026

---

## Step 3: What Does Each Table Represent?

| Table | What a single record represents |
|---|---|
| categories | One product category (e.g. Seafood). There are 8 categories. |
| customers | One customer company that purchases from Northwind Traders. There are 93 customers. |
| employees | One employee who works at Northwind Traders. There are 9 employees. |
| employeeterritories | One assignment linking an employee to a sales territory. There are 49 assignments. |
| order details | One line item within an order (a specific product, quantity, and price). There are 2155 line items. |
| orders | One order placed by a customer. There are 830 orders. |
| products | One product sold by Northwind Traders. There are 77 products. |
| region | One geographic sales region. There are 4 regions. |
| shippers | One shipping company used to deliver orders. There are 3 shippers. |
| suppliers | One supplier that provides products to Northwind Traders. There are 29 suppliers. |
| territories | One sales territory within a region. There are 53 territories. |

---

## Step 4: Record Ratio Check
**Is the ratio of records between tables consistent with what you expected?**

Yes, the ratio of records is consistent with what I expected because logically, 
orders will always exceed the number of customers because one company can place 
multiple orders over time. A database with a 1:1 ratio between customers and 
orders isn't logical. The same logic applies to order details vs orders, since 
one order can have multiple line items. The ratios reflect how a real trading 
company's data would naturally be distributed.

---

## Step 6: Table Information Panel Notes

### categories
- **Primary Key**: CategoryID (int)
- **Parent Tables (Foreign Keys point to)**: None

### customers
- **Primary Key**: CustomerID (varchar(5))
- **Parent Tables (Foreign Keys point to)**: None

### employees
- **Primary Key**: EmployeeID (int)
- **Parent Tables (Foreign Keys point to)**: employees (ReportsTo → EmployeeID)

### employeeterritories
- **Primary Key**: EmployeeID + TerritoryID (composite)
- **Parent Tables (Foreign Keys point to)**: employees (EmployeeID), territories (TerritoryID)

### order details
- **Primary Key**: OrderID + ProductID (composite)
- **Parent Tables (Foreign Keys point to)**: orders (OrderID), products (ProductID)

### orders
- **Primary Key**: OrderID (int)
- **Parent Tables (Foreign Keys point to)**: customers (CustomerID), employees (EmployeeID), shippers (ShipVia)

### products
- **Primary Key**: ProductID (int)
- **Parent Tables (Foreign Keys point to)**: suppliers (SupplierID), categories (CategoryID)

### region
- **Primary Key**: RegionID (int)
- **Parent Tables (Foreign Keys point to)**: None

### shippers
- **Primary Key**: ShipperID (int)
- **Parent Tables (Foreign Keys point to)**: None

### suppliers
- **Primary Key**: SupplierID (int)
- **Parent Tables (Foreign Keys point to)**: None

### territories
- **Primary Key**: TerritoryID (varchar)
- **Parent Tables (Foreign Keys point to)**: region (RegionID)

---

## Step 7: Column-by-Column Notes

---

### categories

**CategoryID**
- **Represents**: A unique number assigned to each category
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed to join to the products table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregating

**CategoryName**
- **Represents**: The name of the actual category (e.g. Beverages, Seafood)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is a useful label for grouping and filtering in reports
- **Good Name?**: A better name for Power BI is simply Category
- **Power BI Data Type**: Text
- **Possible Calculations**: Group/filter total sales by category

**Description**
- **Represents**: A long text description of the category
- **PK**: No | **FK**: No
- **Keep**: No because it is not relevant to sales metric analysis

**Picture**
- **Represents**: A binary image file of the category
- **PK**: No | **FK**: No
- **Keep**: No because it is binary data, not usable in Power BI analysis

---

### customers

**CustomerID**
- **Represents**: A unique identifier assigned to each customer
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is a primary key needed to join on to the orders table
- **Good Name?**: Yes
- **Power BI Data Type**: Text
- **Possible Calculations**: Used for joining, not aggregation

**CompanyName**
- **Represents**: The name of actual client companies (e.g. Bottom-Dollar Markets)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is a useful label for grouping and filtering sales
- **Good Name?**: A better name would be Customer
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total sales by company

**ContactName**
- **Represents**: The name of the representative for each company
- **PK**: No | **FK**: No
- **Keep**: No because sales are tied to the company not the contact

**ContactTitle**
- **Represents**: The role of the representative for each company
- **PK**: No | **FK**: No
- **Keep**: No because it is not relevant to analysis

**Address**
- **Represents**: The street address for each client company
- **PK**: No | **FK**: No
- **Keep**: No because it is too specific, not useful for analysis

**City**
- **Represents**: The city where each client company is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to compare sales across companies 
  in the same city and identify top spenders for targeted marketing
- **Good Name?**: A better name would be Customer City
- **Power BI Data Type**: Text
- **Possible Calculations**: Group/filter total sales by city

**Region**
- **Represents**: The region where each client company is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to compare sales across companies 
  in the same region and identify top spenders for targeted marketing
- **Good Name?**: A better name would be Customer Region
- **Power BI Data Type**: Text
- **Possible Calculations**: Group/filter total sales by region

**PostalCode**
- **Represents**: The postal code for each client company
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for geographic filtering at a granular level
- **Good Name?**: A better name would be Customer Postal Code
- **Power BI Data Type**: Text
- **Possible Calculations**: Group/filter sales by postal code

**Country**
- **Represents**: The country where each client company is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for comparing sales performance across countries
- **Good Name?**: A better name would be Customer Country
- **Power BI Data Type**: Text
- **Possible Calculations**: Group/filter total sales by country

**Phone**
- **Represents**: The phone number of the client company
- **PK**: No | **FK**: No
- **Keep**: No because it is contact info, not useful for analysis

**Fax**
- **Represents**: The fax number of the client company
- **PK**: No | **FK**: No
- **Keep**: No because it is contact info, not useful for analysis

---

### employees

**EmployeeID**
- **Represents**: A unique identifier for each employee
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is a primary key needed to join on to 
  orders and employeeterritories
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**LastName**
- **Represents**: The surname of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it would be more efficient to concatenate 
  with FirstName into a single full name column

**FirstName**
- **Represents**: The first name of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it would be more efficient to concatenate 
  with LastName into a single full name column

> Note: LastName and FirstName will be concatenated into a new 
> calculated column called "Employee Description" in Power Query (Exercise 3B)

**Title**
- **Represents**: The job title of each employee (e.g. Sales Representative)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for filtering sales performance by role
- **Good Name?**: A better name would be Employee Title
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total sales by job title

**TitleOfCourtesy**
- **Represents**: The honorific for each employee (e.g. Ms., Dr.)
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to address employees correctly 
  in reports and visuals
- **Good Name?**: A better name would be Employee Title Of Courtesy
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**BirthDate**
- **Represents**: The date of birth of each employee
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to calculate employee age
- **Good Name?**: A better name would be Employee Birth Date
- **Power BI Data Type**: Date
- **Possible Calculations**: Calculate employee age using DATEDIFF

**HireDate**
- **Represents**: The date each employee was hired
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to calculate years employed
- **Good Name?**: A better name would be Employee Hire Date
- **Power BI Data Type**: Date
- **Possible Calculations**: Calculate years employed using DATEDIFF

**Address**
- **Represents**: The street address of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it is too specific and not relevant to analysis

**City**
- **Represents**: The city where each employee lives
- **PK**: No | **FK**: No
- **Keep**: Yes because geographic data at this level can be used 
  to map employee distribution
- **Good Name?**: A better name would be Employee City
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**Region**
- **Represents**: The region where each employee lives
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to group employees by region
- **Good Name?**: A better name would be Employee Region
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**PostalCode**
- **Represents**: The postal code where each employee lives
- **PK**: No | **FK**: No
- **Keep**: Yes because it provides granular geographic detail
- **Good Name?**: A better name would be Employee Postal Code
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**Country**
- **Represents**: The country where each employee lives
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to group employees by country
- **Good Name?**: A better name would be Employee Country
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**HomePhone**
- **Represents**: The home phone number of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it is contact info that is not useful for analysis

**Extension**
- **Represents**: The office phone extension of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it is contact info, not useful for analysis

**Photo**
- **Represents**: A binary image file of each employee
- **PK**: No | **FK**: No
- **Keep**: No because it is binary data, not usable in Power BI

**Notes**
- **Represents**: A long text bio for each employee
- **PK**: No | **FK**: No
- **Keep**: No because it is long descriptive text that is not useful for analysis

**ReportsTo**
- **Represents**: The EmployeeID of the manager this employee reports to
- **PK**: No | **FK**: Yes, references employees (EmployeeID)
- **Keep**: Yes because it is needed to define the employee hierarchy
- **Good Name?**: A better name would be EmployeeReportsToEmployeeId
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for hierarchy/joining, not aggregation

**PhotoPath**
- **Represents**: The file path to each employee's photo
- **PK**: No | **FK**: No
- **Keep**: No because it is not useful for analysis

**Salary**
- **Represents**: The salary of each employee
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to calculate employee cost 
  against revenue generated
- **Good Name?**: A better name would be Employee Salary
- **Power BI Data Type**: Fixed Decimal ($)
- **Possible Calculations**: Calculate cost per employee against 
  revenue generated

---

### employeeterritories

**EmployeeID**
- **Represents**: A unique identifier for each employee
- **PK**: Yes (composite) | **FK**: Yes, references employees (EmployeeID)
- **Keep**: Yes because it is needed for joining on to the employees table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Grouping/filtering by employee

**TerritoryID**
- **Represents**: A unique identifier for each territory
- **PK**: Yes (composite) | **FK**: Yes, references territories (TerritoryID)
- **Keep**: Yes because it is needed for joining on to the territories table
- **Good Name?**: Yes
- **Power BI Data Type**: Text
- **Possible Calculations**: Grouping/filtering sales by territory 
  and in conjunction with employees

---

### orderdetails

**OrderID**
- **Represents**: A unique identifier for each order
- **PK**: Yes (composite) | **FK**: Yes, references orders (OrderID)
- **Keep**: Yes because it is needed for joining on to the orders table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**ProductID**
- **Represents**: A unique identifier for each product
- **PK**: Yes (composite) | **FK**: Yes, references products (ProductID)
- **Keep**: Yes because it is needed for joining on to the products table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**UnitPrice**
- **Represents**: The price per unit for each product on this order line item
- **PK**: No | **FK**: No
- **Keep**: Yes because it is necessary for determining sales performance
- **Good Name?**: A better name would be Unit Price
- **Power BI Data Type**: Fixed Decimal ($)
- **Possible Calculations**: Calculate total revenue per product by 
  multiplying unit price by quantity

**Quantity**
- **Represents**: The number of units sold for each product on this line item
- **PK**: No | **FK**: No
- **Keep**: Yes because it is necessary for determining units sold 
  and revenue generated
- **Good Name?**: A better name would be Sales Quantity
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Calculate total revenue per product 
  based on units sold

**Discount**
- **Represents**: The discount percentage applied to a product on this order
- **PK**: No | **FK**: No
- **Keep**: Yes because it directly impacts actual revenue and it is needed 
  to calculate the real sales amount after discounts are applied
- **Good Name?**: A better name would be Sales Discount Percent
- **Power BI Data Type**: Percentage
- **Possible Calculations**: Calculate discounted sales amount using 
  unit price, quantity, and discount percent

---

### orders

**OrderID**
- **Represents**: A unique identifier for every order
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed for joining on to orderdetails
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**CustomerID**
- **Represents**: A unique identifier for every customer
- **PK**: No | **FK**: Yes, references customers (CustomerID)
- **Keep**: Yes because it is needed for joining on to the customers table
- **Good Name?**: Yes
- **Power BI Data Type**: Text
- **Possible Calculations**: Used for joining, not aggregation

**EmployeeID**
- **Represents**: A unique identifier for every employee
- **PK**: No | **FK**: Yes, references employees (EmployeeID)
- **Keep**: Yes because it is needed for joining on to the employees table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**OrderDate**
- **Represents**: The date an order was placed
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for tracking transactions over time
- **Good Name?**: A better name would be Order Date
- **Power BI Data Type**: Date
- **Possible Calculations**: Calculate total sales over time and compare 
  sales across months and years

**RequiredDate**
- **Represents**: The date an order is required to be delivered by
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to measure on-time delivery performance
- **Good Name?**: A better name would be Order Required Date
- **Power BI Data Type**: Date
- **Possible Calculations**: Calculate delivery delays by comparing 
  RequiredDate to ShippedDate

**ShippedDate**
- **Represents**: The date an order was shipped from the facility
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to measure shipping speed 
  and on-time delivery
- **Good Name?**: A better name would be Order Shipped Date
- **Power BI Data Type**: Date
- **Possible Calculations**: Calculate days to ship by comparing 
  ShippedDate to OrderDate

**ShipVia**
- **Represents**: The ID of the shipping company used to deliver the order
- **PK**: No | **FK**: Yes, references shippers (ShipperID)
- **Keep**: Yes because it is needed for joining on to the shippers table
- **Good Name?**: A better name would be ShipperID
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Group total orders or freight cost 
  by shipping company

**Freight**
- **Represents**: The shipping cost charged for delivering the order
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for analyzing shipping costs 
  against revenue
- **Good Name?**: A better name would be Order Freight Amount
- **Power BI Data Type**: Fixed Decimal ($)
- **Possible Calculations**: Calculate total freight cost by region, 
  shipper, or time period

**ShipName**
- **Represents**: The name of the recipient the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: Yes because it identifies who received the shipment
- **Good Name?**: A better name would be Order Ship Name
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**ShipAddress**
- **Represents**: The street address the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: No because it is too specific, not useful for analysis

**ShipCity**
- **Represents**: The city the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to analyze sales distribution by city
- **Good Name?**: A better name would be Order Ship City
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total orders or revenue by ship city

**ShipRegion**
- **Represents**: The region the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to analyze sales distribution by region
- **Good Name?**: A better name would be Order Ship Region
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total orders or revenue by ship region

**ShipPostalCode**
- **Represents**: The postal code the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: Yes because it provides granular geographic detail 
  for shipping analysis
- **Good Name?**: A better name would be Order Ship Postal Code
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**ShipCountry**
- **Represents**: The country the order was shipped to
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to analyze international 
  sales distribution
- **Good Name?**: A better name would be Order Ship Country
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total orders or revenue by ship country

---

### products

**ProductID**
- **Represents**: A unique identifier for each product
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is necessary for joining on to the orderdetails table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**ProductName**
- **Represents**: The name of every individual product
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to rank top performing products by revenue
- **Good Name?**: A better name would be Product
- **Power BI Data Type**: Text
- **Possible Calculations**: Group aggregations like revenue per product 
  based on sales amounts

**SupplierID**
- **Represents**: A unique identifier for every supplier
- **PK**: No | **FK**: Yes, references suppliers (SupplierID)
- **Keep**: Yes because it is necessary to join on to the suppliers table 
  to see which suppliers provide which products
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**CategoryID**
- **Represents**: A unique identifier for every category
- **PK**: No | **FK**: Yes, references categories (CategoryID)
- **Keep**: Yes because it is necessary to join on to the categories table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**QuantityPerUnit**
- **Represents**: How the product is packaged and sold 
  (e.g. 10 boxes x 20 bags)
- **PK**: No | **FK**: No
- **Keep**: Yes because it provides context for how products are sold
- **Good Name?**: A better name would be Product Quantity Per Unit
- **Power BI Data Type**: Text
- **Possible Calculations**: None

**UnitPrice**
- **Represents**: The current listed price per unit for every product
- **PK**: No | **FK**: No
- **Keep**: Yes because it is needed to compare current prices against 
  historical sale prices in orderdetails
- **Good Name?**: A better name would be Product Current Unit Price
- **Power BI Data Type**: Fixed Decimal ($)
- **Possible Calculations**: Compare current unit price against historical 
  sale prices to analyze pricing changes over time

**UnitsInStock**
- **Represents**: The number of units currently available in inventory
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for inventory analysis
- **Good Name?**: A better name would be Product Units In Stock
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Calculate inventory value by multiplying 
  units in stock by unit price

**UnitsOnOrder**
- **Represents**: The number of units currently on order from the supplier
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for supply chain and inventory 
  planning analysis
- **Good Name?**: A better name would be Product Units On Order
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Compare units on order against units in stock 
  to identify potential stock shortages

**ReorderLevel**
- **Represents**: The minimum stock level that triggers a reorder 
  from the supplier
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to flag products running low on stock
- **Good Name?**: A better name would be Product Reorder Level
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Flag products where units in stock are at or 
  below the reorder level

**Discontinued**
- **Represents**: A flag indicating whether a product is no longer being 
  sold (1 = discontinued, 0 = active)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful for filtering out discontinued products 
  from active sales analysis
- **Good Name?**: A better name would be Product Discontinued
- **Power BI Data Type**: True/False
- **Possible Calculations**: Filter active vs discontinued products when 
  analyzing sales performance

---

### region

**RegionID**
- **Represents**: A unique identifier for each region
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed for joining on to the territories table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**RegionDescription**
- **Represents**: The name of each region (e.g. Eastern, Western)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is a short label useful for grouping and 
  filtering sales by region in reports
- **Good Name?**: A better name would be Region
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total sales by region

---

### shippers

**ShipperID**
- **Represents**: A unique identifier for each shipper
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed for joining on to the orders table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**CompanyName**
- **Represents**: The name of each shipping company
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to filter and compare orders 
  by shipping company
- **Good Name?**: A better name would be Shipper
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total orders and freight cost by shipper

**Phone**
- **Represents**: The phone number of each shipping company
- **PK**: No | **FK**: No
- **Keep**: No because contact info is not useful for analysis

---

### suppliers

**SupplierID**
- **Represents**: A unique identifier for each supplier
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed for joining on to the products table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

**CompanyName**
- **Represents**: The name of each supplier company
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to filter and compare products 
  by supplier
- **Good Name?**: A better name would be Supplier
- **Power BI Data Type**: Text
- **Possible Calculations**: Group total products and orders by supplier

**ContactName**
- **Represents**: The name of the representative for each supplier company
- **PK**: No | **FK**: No
- **Keep**: Yes because it is necessary to group supplied products 
  authorized by a specific person
- **Good Name?**: A better name would be Supplier Contact
- **Power BI Data Type**: Text
- **Possible Calculations**: Group supplied products by contact

**ContactTitle**
- **Represents**: The job role of each contact representative for 
  each supplier company
- **PK**: No | **FK**: No
- **Keep**: Yes because it is useful to reference contacts by their role 
  and analyze whether higher ranked titles supply more premium products
- **Good Name?**: A better name would be Supplier Contact Title
- **Power BI Data Type**: Text
- **Possible Calculations**: Group supplied products by contact role

**Address**
- **Represents**: The street address of each supplier company
- **PK**: No | **FK**: No
- **Keep**: No because it is too granular, not useful for analysis

**City**
- **Represents**: The city where each supplier is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used to filter suppliers by city
- **Good Name?**: A better name would be Supplier City
- **Power BI Data Type**: Text
- **Possible Calculations**: Group number of suppliers by city

**Region**
- **Represents**: The region where each supplier is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used for cross-region analysis 
  based on highest volume suppliers
- **Good Name?**: A better name would be Supplier Region
- **Power BI Data Type**: Text
- **Possible Calculations**: Group suppliers by region

**PostalCode**
- **Represents**: The postal code for each supplier
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used for granular geographic analysis
- **Good Name?**: A better name would be Supplier Postal Code
- **Power BI Data Type**: Text
- **Possible Calculations**: Group suppliers by postal code

**Country**
- **Represents**: The country where each supplier is based
- **PK**: No | **FK**: No
- **Keep**: Yes because it can be used for filtering top suppliers by country
- **Good Name?**: A better name would be Supplier Country
- **Power BI Data Type**: Text
- **Possible Calculations**: Group suppliers by country

**Phone**
- **Represents**: The phone number for each supplier contact
- **PK**: No | **FK**: No
- **Keep**: No because contact info is not relevant to analysis

**Fax**
- **Represents**: The fax number for each supplier contact
- **PK**: No | **FK**: No
- **Keep**: No because contact info is not relevant to analysis

**HomePage**
- **Represents**: The website or description for each supplier company
- **PK**: No | **FK**: No
- **Keep**: No because long text descriptions are not useful for analysis

---

### territories

**TerritoryID**
- **Represents**: A unique identifier for each territory
- **PK**: Yes | **FK**: No
- **Keep**: Yes because it is needed to join on to employeeterritories
- **Good Name?**: Yes
- **Power BI Data Type**: Text
- **Possible Calculations**: Used for joining, not aggregation

**TerritoryDescription**
- **Represents**: The name of each territory (e.g. state names)
- **PK**: No | **FK**: No
- **Keep**: Yes because it is necessary for filtering sales by territory 
  and comparing performance within regions
- **Good Name?**: A better name would be Territory
- **Power BI Data Type**: Text
- **Possible Calculations**: Group revenue by territory for regional 
  sales comparison

**RegionID**
- **Represents**: A unique identifier for each region
- **PK**: No | **FK**: Yes, references region (RegionID)
- **Keep**: Yes because it is needed for joining on to the region table
- **Good Name?**: Yes
- **Power BI Data Type**: Whole Number
- **Possible Calculations**: Used for joining, not aggregation

---

## Key Takeaway | Fact vs Lookup Tables

When exploring a database schema, you can identify fact and lookup tables 
just by looking at their foreign keys:

**Fact Tables** (e.g. orders, orderdetails):
- Have the most foreign keys pointing outward to other tables
- Record events or transactions that happen at a point in time
- Example: `orders` points to customers, employees, and shippers — 
  it's recording a transaction that happened

**Lookup Tables** (e.g. customers, products, suppliers):
- Have no foreign keys — they just sit there with their own PK
- Describe things that exist, not events that happen
- Example: `customers` just describes who a customer is — 
  it doesn't record anything happening

**How to spot a composite PK vs a regular PK:**
- If a table has its own identity (like an order), it gets its own 
  unique ID → single PK
- If a table only makes sense in the context of two other things 
  (like a line item needing both an order AND a product), those two 
  FKs together form the PK → composite PK

**How to spot a FK without it being labeled:**
- Column named `[TableName]ID` almost always points to that table
- Table named `[Thing1][Thing2]` with two ID columns = junction table
- A column with an int data type matching another table's PK 
  (like `ReportsTo` matching `EmployeeID`) is a self-referencing FK
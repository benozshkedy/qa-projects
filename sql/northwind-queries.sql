-- 1. All customers from USA
SELECT CustomerID, CompanyName, City, Country
FROM Customers
WHERE Country = 'USA';

-- 2. Products with price above 50$
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50
ORDER BY UnitPrice DESC;

-- 3. Employees born after 1960
SELECT FirstName, LastName, BirthDate
FROM Employees
WHERE BirthDate > '1960-01-01';

-- 4. Orders with customer name
SELECT o.OrderID, c.CompanyName, o.OrderDate
FROM Orders o
INNER JOIN Customers c
    ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC;

-- 5. Product with its category
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM Products p
INNER JOIN Categories c
    ON p.CategoryID = c.CategoryID;

-- 6. Suppliers without products
SELECT s.CompanyName
FROM Suppliers s
LEFT JOIN Products p
    ON s.SupplierID = p.SupplierID
WHERE p.ProductID IS NULL;

-- 7. Number of orders per customer
SELECT c.CompanyName, COUNT(o.OrderID) AS TotalOrders
FROM Customers c
LEFT JOIN Orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY TotalOrders DESC;

-- 8. Average product price per category
SELECT c.CategoryName, AVG(p.UnitPrice) AS AvgPrice
FROM Categories c
INNER JOIN Products p
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 9. Total amount per order
SELECT od.OrderID,
       SUM(od.UnitPrice * od.Quantity) AS OrderTotal
FROM [Order Details] od
GROUP BY od.OrderID
ORDER BY OrderTotal DESC;

-- 10. Products never ordered
SELECT p.ProductName
FROM Products p
LEFT JOIN [Order Details] od
    ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;

-- 11. Late shipments (ShippedDate > RequiredDate)
SELECT OrderID, RequiredDate, ShippedDate
FROM Orders
WHERE ShippedDate > RequiredDate;

-- 12. Top 5 customers by number of orders
SELECT TOP 5 c.CompanyName,
       COUNT(o.OrderID) AS TotalOrders
FROM Customers c
INNER JOIN Orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY TotalOrders DESC;

-- 13. Products priced above average
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);

-- 14. Customer with the most expensive order
SELECT TOP 1 c.CompanyName,
       SUM(od.UnitPrice * od.Quantity) AS OrderTotal
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CompanyName, o.OrderID
ORDER BY OrderTotal DESC;


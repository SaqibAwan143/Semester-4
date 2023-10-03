
--task 1
SELECT CustomerID, CompanyName AS CustomerName
FROM Customers
WHERE CustomerID IN (
  SELECT DISTINCT CustomerID
  FROM Orders
  WHERE ShippedDate > RequiredDate
)
ORDER BY CustomerID;

---task2
SELECT ProductName, SupplierName
FROM (
  SELECT p.ProductName, s.CompanyName AS SupplierName, p.SupplierID
  FROM Products p
  JOIN Suppliers s ON p.SupplierID = s.SupplierID
) AS ProductSupplier
ORDER BY ProductName;

---task3
SELECT TOP 10 ProductName, TotalSales
FROM (
  SELECT p.ProductName, SUM(od.Quantity * od.UnitPrice) AS TotalSales
  FROM Products p
  JOIN [Order Details] od ON p.ProductID = od.ProductID
  JOIN Orders o ON od.OrderID = o.OrderID
  WHERE YEAR(o.OrderDate) = 1998
  GROUP BY p.ProductName
) AS ProductSales
ORDER BY TotalSales DESC;

--task 4	
SELECT e.FirstName + ' ' + e.LastName AS EmployeeName, (
  SELECT m.FirstName + ' ' + m.LastName
  FROM Employees m
  WHERE e.ReportsTo = m.EmployeeID
) AS ManagerName
FROM Employees e
ORDER BY ManagerName, EmployeeName;

---task 5
SELECT CONCAT(e1.FirstName, ' ', e1.LastName) AS ManagerFullName
FROM Employees e1
WHERE e1.EmployeeID IN (
  SELECT e2.ReportsTo
  FROM Employees e2
  GROUP BY e2.ReportsTo
  HAVING COUNT(*) < 2
)

--task 6
SELECT * 
FROM Products
WHERE UnitPrice > (
  SELECT AVG(UnitPrice) 
  FROM Products
)

---task 7
SELECT ProductName, UnitPrice as Price 
FROM Products 
WHERE UnitPrice = (
    SELECT MAX(UnitPrice) 
    FROM Products 
    WHERE UnitPrice < (
        SELECT MAX(UnitPrice) 
        FROM Products
    )
);


--task 8
SELECT 
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
    CONCAT(m.FirstName, ' ', m.LastName) AS ManagerName,
    YEAR(GETDATE()) - YEAR(e.BirthDate) - IIF(MONTH(GETDATE()) < MONTH(e.BirthDate), 1, IIF(MONTH(GETDATE()) = MONTH(e.BirthDate) AND DAY(GETDATE()) < DAY(e.BirthDate), 1, 0)) AS EmployeeAge,
    YEAR(GETDATE()) - YEAR(m.BirthDate) - IIF(MONTH(GETDATE()) < MONTH(m.BirthDate), 1, IIF(MONTH(GETDATE()) = MONTH(m.BirthDate) AND DAY(GETDATE()) < DAY(m.BirthDate), 1, 0)) AS ManagerAge
FROM 
    Employees e
    JOIN Employees m ON e.ReportsTo = m.EmployeeID
WHERE 
    e.BirthDate < m.BirthDate
ORDER BY 
    EmployeeAge DESC;

SELECT e.FirstName + ' ' + e.LastName AS EmployeeName
FROM Employees e
WHERE e.BirthDate > (
  SELECT m.BirthDate
  FROM Employees m
  WHERE m.EmployeeID = e.ReportsTo
);


---task 9
SELECT ProductName
FROM Products
WHERE ProductID IN (
    SELECT ProductID
    FROM [Order Details]
    WHERE OrderID IN (
        SELECT OrderID
        FROM Orders
        WHERE OrderDate = '1997-08-08'
    )
);

--task 10
SELECT DISTINCT CompanyName
FROM Suppliers
WHERE SupplierID IN (
    SELECT SupplierID
    FROM Products
    WHERE ProductID IN (
        SELECT ProductID
        FROM [Order Details]
        WHERE OrderID IN (
            SELECT OrderID
            FROM Orders
            WHERE OrderDate BETWEEN '1997-01-01' AND '1997-12-31'
        )
    )
);

--task 11
SELECT COUNT(*)
FROM Employees
WHERE EmployeeID IN (
    SELECT EmployeeID
    FROM EmployeeTerritories
    WHERE TerritoryID IN (
        SELECT TerritoryID
        FROM Territories
        WHERE RegionID = 3
    )
);

--task 12
SELECT ProductName
FROM Products
WHERE ProductID NOT IN (
    SELECT ProductID
    FROM [Order Details]
    WHERE OrderID IN (
        SELECT OrderID
        FROM Orders
        WHERE OrderDate BETWEEN '1996-01-01' AND '1996-12-31'
    )
);





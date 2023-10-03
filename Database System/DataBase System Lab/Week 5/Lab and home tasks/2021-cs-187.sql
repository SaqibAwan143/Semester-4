--task 1
SELECT c.CustomerID, o.OrderID, o.OrderDate 
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
ORDER BY c.CustomerID;

--task2
SELECT Customers.CustomerID
FROM Customers
LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;

--task3 
SELECT Customers.CustomerID, Orders.OrderID, Orders.OrderDate
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderDate >= '1997-07-01' AND Orders.OrderDate < '1997-08-01';

--task4
SELECT c.CustomerID, COUNT(o.OrderID) as totalorders
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID

--task 5
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e
CROSS JOIN (
    SELECT 1 AS num UNION ALL
    SELECT 2 AS num UNION ALL
    SELECT 3 AS num UNION ALL
    SELECT 4 AS num UNION ALL
    SELECT 5 AS num
) n
ORDER BY e.EmployeeID, n.num

--task6
SELECT Employees.EmployeeID, DATEADD(day, Number - 1, '1996-04-07') AS Date
FROM Employees
CROSS JOIN (
  SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS Number
  FROM sys.columns
) AS Numbers
WHERE DATEADD(day, Number - 1, '1996-04-07') <= '1997-04-08'
ORDER BY Employees.EmployeeID, Date;

--task7
SELECT 
    o.CustomerID,
    COUNT(o.OrderID) AS TotalOrders,
    SUM(od.Quantity) AS TotalQuantity
FROM 
    Orders o
    JOIN [Order Details] od ON o.OrderID = od.OrderID
WHERE 
    o.CustomerID IS NOT NULL and o.ShipCity = 'US'
GROUP BY 
    o.CustomerID

--task8
 SELECT c.CustomerID, c.CompanyName, o.OrderID, o.OrderDate 
FROM Customers c 
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID 
WHERE o.OrderDate = '1997-07-04'

--task9
--Are there any employees who are older than their managers? 
SELECT e.FirstName AS EmployeeFirstName, e.LastName AS EmployeeLastName, e.BirthDate AS EmployeeBirthDate, 
m.FirstName AS ManagerFirstName, m.LastName AS ManagerLastName, m.BirthDate AS ManagerBirthDate
FROM Employees e
INNER JOIN Employees m ON e.ReportsTo = m.EmployeeID
WHERE e.BirthDate < m.BirthDate;

--task10  List that names of those employees and their ages. (EmployeeName, Age, Manager Age)	SELECT CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
		   YEAR(GETDATE()) - YEAR(e.BirthDate) - (MONTH(GETDATE()) < MONTH(e.BirthDate) OR (MONTH(GETDATE()) = MONTH(e.BirthDate) AND DAY(GETDATE()) < DAY(e.BirthDate))) AS EmployeeAge,
		   YEAR(GETDATE()) - YEAR(m.BirthDate) - (MONTH(GETDATE()) < MONTH(m.BirthDate) OR (MONTH(GETDATE()) = MONTH(m.BirthDate) AND DAY(GETDATE()) < DAY(m.BirthDate))) AS ManagerAge
	FROM Employees e
	INNER JOIN Employees m ON e.ReportsTo = m.EmployeeID
	WHERE e.BirthDate < m.BirthDate;

--task11   • List the names of products which were ordered on 8th August 1997. (ProductName, OrderDate)
SELECT Products.ProductName, Orders.OrderDate
FROM Products
INNER JOIN [Order Details] ON Products.ProductID = [Order Details].ProductID
INNER JOIN Orders ON [Order Details].OrderID = Orders.OrderID
WHERE CONVERT(date, Orders.OrderDate) = '1997-08-08';

--task12
SELECT ShipAddress AS Address, ShipCity AS City, ShipCountry AS Country
FROM Orders
WHERE EmployeeID = (
  SELECT EmployeeID
  FROM Employees
  WHERE FirstName = 'Anne'
) AND ShippedDate > RequiredDate;

--task13 • List all countries to which beverages have been shipped. (Country)
SELECT DISTINCT ShipCountry AS Country
FROM Orders
JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID
JOIN Products ON [Order Details].ProductID = Products.ProductID
WHERE Products.CategoryID = 1;








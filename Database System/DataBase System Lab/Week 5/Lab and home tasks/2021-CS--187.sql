--task 1
----inner join
select od.OrderID,o.CustomerID,p.ProductName
from [Order Details] od
inner join Orders o
on od.OrderID = o.OrderID
inner join Products p 
on od.ProductID = p.ProductID

----2. Left Join  "What are the OrderID, CompanyName, and ProductName for all orders in the Orders table?"
SELECT Orders.OrderID, Customers.CompanyName, Products.ProductName 
FROM Orders
LEFT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
LEFT JOIN [Order Details]
ON Orders.OrderID = [Order Details].OrderID
LEFT JOIN Products
ON [Order Details].ProductID = Products.ProductID;

--3. Right Join " the total number of orders placed by customers  "

SELECT COUNT(o.OrderID)
FROM Orders o
RIGHT JOIN Customers c
ON o.CustomerID = c.CustomerID;


---4. Full Join What are the customer names, orders, and order dates for orders placed in July 1996 

SELECT Customers.CustomerName, Orders.OrderID, Orders.OrderDate
FROM Customers
FULL JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
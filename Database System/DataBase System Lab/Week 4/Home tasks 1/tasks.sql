---Query 1
select Products.ProductName
from Products
group by ProductName,UnitPrice
having UnitPrice > AVG(UnitPrice)


---Query 2
select * 
from Orders
where ShippedDate is not NULL 
order by ShippedDate asc


---Query 3
---method 1
select s.Country
from Suppliers s, Suppliers s1
where s.Country = s1.Country
group by s.Country
having count(s.Country) > 2


----method 2
SELECT Country
FROM Suppliers
GROUP BY Country
HAVING COUNT(*) > 1;

---Query 4
SELECT MONTH(ShippedDate) AS 'Month Number', COUNT(OrderID) AS 'Orders Delayed'
FROM Orders
WHERE ShippedDate > RequiredDate
GROUP BY MONTH(ShippedDate);

---Query 5
SELECT OrderID, SUM(Discount) AS 'Discount'
FROM [Order Details]
WHERE Discount > 0
GROUP BY OrderID;

---Query 6

SELECT ShipCity, COUNT(OrderID) AS NumberOfOrders
FROM Orders
WHERE ShipCountry = 'USA' AND YEAR(ShippedDate) = 1997
GROUP BY ShipCity;

---Query 7

SELECT ShipCountry, COUNT(*) AS 'Orders Delayed'
FROM Orders
WHERE ShippedDate > RequiredDate
GROUP BY ShipCountry

---Query 8

SELECT Orders.OrderID, SUM(Discount) as Discount, SUM([Order Details].UnitPrice * Quantity) as TotalPrice
FROM Orders
JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID
GROUP BY  Orders.OrderID

---Query 9

SELECT ShipRegion, ShipCity, COUNT(OrderID) AS Orders
FROM Orders
WHERE YEAR(ShippedDate) = 1997
GROUP BY ShipRegion, ShipCity;
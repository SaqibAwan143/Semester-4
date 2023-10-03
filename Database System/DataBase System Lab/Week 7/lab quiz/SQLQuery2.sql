;
----
SELECT o.ShipCity AS City, 
       COUNT(o.OrderID) - COUNT(o.ShippedDate) AS CountofPendingorders, 
       COUNT(o.ShippedDate) AS CountofShippedorders 
FROM Orders o 
GROUP BY o.ShipCity;


----some customers like particular category than other category.Display the name of category against each customer ,whose maximum products have been ordered by him.
--task 2
SELECT oc.CustomerID, c.CategoryName 
FROM Categories oc 
INNER JOIN Categories c ON oc.CategoryID = c.CategoryID 
GROUP BY oc.CustomerID, c.CategoryName 
HAVING COUNT(oc.OrderID) = (SELECT MAX(t.max_orders) 
                            FROM (SELECT COUNT(oc2.OrderID) AS max_orders 
                                  FROM Categories oc2 
                                  GROUP BY oc2.CustomerID) t);



write a query to display employees names whode managers were hired before employee itself.display name of empoyees only using northwind schema

---task 4


select * 
from Employees


write a query to display which city has maximum customers.Shema contains the city name only using northwind schema
--task3
select ShipCity as city
from Orders
group by ShipCity


SELECT o.ShipCity AS City, COUNT(o.OrderID) AS Customers 
FROM Orders o 
GROUP BY o.ShipCity 
ORDER BY Customers DESC 

create database northwind;

--1
select * 
from orders 
where ShippedDate >RequiredDate

--2
select Country
from Employees

--3

--4
select ProductName
From Products
where Discontinued = 1

--5
select OrderID
from [Order Details]
where Discount = 0

--6
select CustomerID
from Customers
where Region is NULL 

--7
select CustomerID ,Phone
from Customers
where Country = 'UK' or Country = 'USA'

--8
select CompanyName
from Suppliers
where HomePage is not NULL

--9
select ShipCountry
from Orders
where ShippedDate >= 1997-1-1 or ShippedDate <= 1997-12-30

--10
select CustomerID
from Orders
where ShippedDate is NULL

--11
select SupplierID,CompanyName,City
from Suppliers

--12
select *
from Employees
where City = 'London'

--13
select ProductName,Discontinued
from Products
where Discontinued =0

--14-------
select OrderID
from [Order Details]
where Discount <= 0.1

--15
select EmployeeID,FirstName,HomePhone,Extension
from Employees
where Region is NULL
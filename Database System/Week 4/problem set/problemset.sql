select * from Company

--1

--m1
select name
from Product 
where cost > (select AVG(cost) from Product)


--m2
select DISTINCT p.name
from Product p,Product p1
where P.cost > (select AVG(cost) from Product)
--we cannot use simple having group by condition for average here because having in group by attributes must be same

--m3
SELECT NAME 
from Product
except
select name
from Product
where cost <= (select AVG(cost) from Product)

--m4
select p1.name 
from Product p1
join Product p2
on p1.name = p2.name 
where p1.cost > (select AVG(cost) from Product)

--m5
SELECT NAME 
from Product
intersect
select name
from Product
where cost > (select AVG(cost) from Product)


------2-----

--m1
select Company.name
from Company
join Product
on Company.name = Product.maker
join Purchase
on product.name = Purchase.product
where Purchase.buyer = 'saqib'

--m2
select Company.name 
from Company
where Company.name in (select Product.maker from Product where Product.name in (select Purchase.product from Purchase where buyer = 'saqib'))

--m3
select  c.name
from Company c,Product,Purchase
where buyer = 'saqib' and (product.name = Purchase.product) and (c.name = maker)

--m4
select Company.name
from Company
intersect
select  c.name
from Company c,Product,Purchase
where buyer = 'saqib' and (product.name = Purchase.product) and (c.name = maker)

--m5*****************
select Company.name
from Company
except
select Company.name
from Company
join Product
on Company.name = Product.maker
join Purchase
on product.name = Purchase.product
where Purchase.buyer <> 'saqib'

select * from Purchase
select * from Product
insert into Product values ('accord','kia',800000,2023)

------3-------

--m1
select name
from Product
where cost > (select sum(cost) from Product where maker = 'honda')

--m2
select p1.name 
from Product p1
join Product p2
on p1.name = p2.name 
where p1.cost > (select sum(cost) from Product where maker = 'honda')

--m3
select distinct p.name
from Product p,Product p1
where P.cost > (select sum(cost) from Product where maker = 'kia')

--m4

SELECT NAME 
from Product
intersect
select name
from Product
where cost > (select sum(cost) from Product where maker = 'kia')

--m5
SELECT NAME 
from Product
except
select name
from Product
where cost <= (select AVG(cost) from Product where maker = 'kia')


------4------

--m1----sub query
select name,maker
from Product
where name in (select name from Product where maker = 'honda') and maker <> 'honda'

--m2----join
select p1.name,p1.maker
from product p1
join product p2
on (p1.name = p2.name) and (p2.maker = 'honda')
where p1.maker <> 'honda'

---m3---cartesian
select p1.name,p2.maker
from product p1,product p2
 where(p1.name = p2.name) and (p1.maker = 'honda') and p2.maker <> 'honda'

 ----m4----intersection*******



 ---m5--*********


--------5-----------

 ---m1--join
select Purchase.buyer
from purchase
join Product
on purchase.product = Product.name
join Company
on Company.name = Product.maker
where Company.city = 'lahore'

--m2--sub query
select Purchase.buyer
from Purchase
where Purchase.product in (select Product.name from Product where Product.maker in (select Company.name from Company where city = 'lahore'))

---m3---cartesian product
select  p.buyer
from Purchase p,Product,Company 
where Company.city = 'lahore' and (p.product = Product.name) and (Product.maker =  Company.name)

--m4--- intersection
select  purchase.buyer
from Purchase
intersect
select  p.buyer
from  Purchase p,Product,Company
where Company.city = 'lahore' and (p.product = Product.name) and (Product.maker =  Company.name)

--m5----except

select  purchase.buyer
from Purchase
except
select  p.buyer
from  Purchase p,Product,Company
where Company.city <> 'lahore' and (p.product = Product.name) and (Product.maker =  Company.name)

----------6--------------

SELECT buyer
FROM Purchase P1
WHERE P1.product IN(
SELECT name
FROM Product Pr1
WHERE Pr1.maker  IN (
SELECT Name
FROM Company C
WHERE C.city = 'Karachi' ))
Except
SELECT buyer
FROM Purchase P1
WHERE P1.product IN(
SELECT name
FROM Product Pr1
WHERE Pr1.maker  IN (
SELECT Name
FROM Company C
WHERE C.city < > 'Karachi' ))

-------m1----
select ph.buyer from Purchase ph
join Product p
on p.name = ph.product
join Company c
on c.name = p.maker
except
select ph.buyer from Purchase ph
join Product p
on p.name = ph.product
join Company c
on c.name = p.maker
where c.city <> 'karachi'

------m3-----

------m4----





---------7----------

-----m1---group by
select Purchase.product,Purchase.price
from Purchase
group by Purchase.product,Purchase.price
having COUNT(Purchase.buyer) > 1

----m2--join

select p.product,p1.price
from Purchase p
join Purchase p1
on (p.product = p1.product) and p.price = p1.price
group by p.product,p1.price
having COUNT(p.buyer) > 1

-----m3-----cartesian
select p.product, p1.price
from Purchase p,Purchase p1
where (p.product = p1.product) and p.price = p1.price
group by p.product,p1.price
having COUNT(p.buyer) > 1

------m4----intersect
select p.product,p1.price
from Purchase p , Purchase p1
where (p.product = p1.product) and p.price = p1.price
group by  p.product,p1.price
intersect
select p.product, p1.price
from Purchase p,Purchase p1
where (p.product = p1.product) and p.price = p1.price
group by p.product,p1.price
having COUNT(p.buyer) > 1

---m5---********



----------8-----------

----m1--sub query
select * from Product p
where p.cost > (select sum(cost) from Product where year < 2015) and year > 2015


----m2--- cartesian 
select * from Product p,Product p1
where p.cost > (select sum(cost) from Product where year < 2015) and p1.year > 2015 and p.name <> p1.name

------m3------***** join
select * from Product p
join Product p1
on p.name = p1.name
where p.year > 2015
group by p.year ,p.cost,p1.cost
having p.cost > sum(p1.cost)

-----m4-------*****
select * from Product
where year > 2015 
except
select sum(cost) from Product
where year < 2015


------9--------

---m1-----cartesian
select distinct c.name
from Company c,Product p, Purchase ph
where c.name = p.maker and p.name = ph.product and Ph.price > p.cost

-----m2----- join
select distinct c.name
from Company c
join Product p 
on c.name = p.maker 
join Purchase ph
on p.name = ph.product
where ph.price > p.cost

-----m3-----except
select distinct c.name
from Company c
join Product p 
on c.name = p.maker 
join Purchase ph
on p.name = ph.product
except
select distinct c.name
from Company c
join Product p 
on c.name = p.maker 
join Purchase ph
on p.name = ph.product
where ph.price < p.cost

----m4-----intersection
select distinct c.name
from Company c
join Product p 
on c.name = p.maker 
join Purchase ph
on p.name = ph.product
intersect
select distinct c.name
from Company c
join Product p 
on c.name = p.maker 
join Purchase ph
on p.name = ph.product
where ph.price > p.cost

-----m5-----
select c.name
from Company c
where C.name in (select p.maker from Product p where p.name in (select ph.product from purchase ph where ph.price > p.cost))

insert into Company values ('ford','islamabad')
insert into Product values ('mustang','ford',220000,2019)
insert into Purchase values (834,'mustang','Azman',210000)

--where c.name in (select p.maker,(select purchase.price from purchase ) from product p 





-----------10--------------

--m1---
--This Query can not be entertained because revenue can be generated only from products saled by a company in a certain period of time .but we are provided only with the product launched date but not the date on which product has been saled .thats why this query canot be written
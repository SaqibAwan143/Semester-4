--QUERY 1
select Stations.Location
from Stations
where Station_ID IN (select Station_ID from Bike_Rentals 
join Payments on Payments.Payment_ID = Bike_Rentals.Payment_ID
where YEAR(Payments.Date_Stamp) = 2004)

--QUERY 2
select *
from (select Bikes.Bike_ID, Repairs.Price as RepairingCost
from Bikes 
join Bike_Status on Bikes.Bike_ID = Bike_Status.Bike_ID
join Repairs on Bike_Status.B_Status_ID = Repairs.B_Status_ID) as B

--QUERY 3
select O.Location
from (SELECT top 3 s.Location
FROM Stations s
JOIN bikes b ON b.station_id = s.station_id
JOIN bike_status bs ON bs.bike_id = b.bike_id
JOIN Repairs r ON r.B_Status_ID = bs.B_Status_ID
GROUP BY s.Location
ORDER BY COUNT( r.repair_id) DESC) as O

--QUERY 4
select O.Location, O.TotalBikesOwned
from (select Stations.Location, COUNT(Bikes.Bike_ID) as TotalBikesOwned
from Stations join Bikes
on Stations.Station_ID = Bikes.Station_ID
group by Stations.Location) as O

--QUERY 5
select O.Fname, o.Lname
from ( select Customer_Details.Fname, Customer_Details.Lname
from Customer_Details full join Bike_Rentals
on Customer_Details.Customer_ID = Bike_Rentals.Customer_ID
where Bike_Rentals.Rental_ID IS NULL) as O

--QUERY 6
select O.Bike_ID
from (select Bike_Rentals.Bike_ID from Bike_Rentals
join Payments on Bike_Rentals.Customer_ID = Payments.Customer_ID
where YEAR(Payments.Date_stamp) > '2016'
group by Bike_Rentals.Bike_ID) as O

--QUERY 7
select o.Fname, O.Lname
from (select Customer_Details.Fname, Customer_Details.Lname from Customer_Details
join Payments on Customer_Details.Customer_ID = Payments.Payment_ID
join Payment_Method on Payment_Method.Method_ID = Payments.Method_ID
where Payment_Method.Method = 'mastercard') as O

--QUERY 8
select Stations.Location, Vans.Bikes
from Stations join Vans
on Stations.Station_ID = Vans.Station_ID
where Vans.Bikes = (select MAX(Vans.Bikes) from Vans)

--QUERY 9
select O.Bike_ID, O.AverageCost
from (select Bike_Status.Bike_ID, AVG(Repairs.Price) as AverageCost from Bike_Status
join Repairs on Repairs.B_Status_ID = Bike_Status.B_Status_ID group by Bike_Status.Bike_ID) as O

--QUERY 10
SELECT O.Bike_ID
FROM ( select Bike_Status.Bike_ID from Bike_Status
INNER JOIN Repairs ON repairs.B_Status_ID = Bike_Status.B_Status_ID
WHERE YEAR(Repairs.Delivered) > 2016) as O

 
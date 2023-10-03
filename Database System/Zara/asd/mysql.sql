create database mobilestore;
use mobilestore;
 
create table mobile(
mobile_id int primary key, 
comp_name varchar(50), 
quantity int, 
mfg_date date, 
price float) ;

create table customer(
cust_id int primary key,
cust_name varchar(40),
cust_address varchar(250),
cust_age int,
cust_phoneno int);

create table billreceipt(
cust_id int,
cust_name varchar(40),
mobile_id int,
total_amtpaid float) ;

create table empl(
empl_id int, 
empl_name varchar(40), 
empl_address varchar(250), 
empl_phoneno int, 
date_of_joining date) ;

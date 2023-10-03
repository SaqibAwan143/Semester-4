create database mobilestore;
use mobilestore;
 
create table mobile(
model_id varchar(30) primary key, 
model_name varchar(50), /////
quantity int, 
mfg_date varchar(100), 
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
mobile_id varchar(30),
total_amtpaid float) ;

create table empl(
empl_id int primary key, 
empl_name varchar(40), 
empl_age int, /////
empl_salary float, ///////
date_of_joining varchar(100)) ;

create database StudentRecord;

create table student (
registration_no varchar(20),
Firstname varchar (20),
lastname varchar(20),
GPA float(10),
contact int,
)

insert into student values('2021-CS-169','Muhammad','Ibrahim',3.67,0343);

select registration_no from student

select Firstname from student

select lastname from student

select GPA from student

select contact from student

select *
from student
where GPA > 3.5

select *
from student
where GPA <= 3.5

select registration_no, Firstname +' '+ lastname
from student


create database Lab2_hometask

create table StuRecord(
RegNumber varchar(20),
Name varchar(20),
Department varchar(20),
Session int,
Address varchar(20)
)

create table Courses(
Course_ID varchar(20),
Course_Name varchar(20),
Student_Name varchar(20),
Teacher_Name varchar(20),
Semester varchar(20)
)

create table Enrollment(
StudentRegNo varchar(20),
CourseName varchar(20),
)

create table Attendances(
StudentRegNo varchar(20),
CourseName varchar(20),
TimeStamp datetime,
Status bit,
Semester varchar(20)
)

select * from Enrollment
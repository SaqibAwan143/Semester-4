create database Lab2_Home

create table Studentdata1(
RegNumber varchar(20),
Name varchar(20),
Department varchar(20),
Session int,
Address varchar(20)
)

create table Course1(
Course_ID varchar(20),
Course_Name varchar(20),
Student_Name varchar(20),
Teacher_Name varchar(20),
Semester varchar(20)
)

create table Enrollments1(
StudentRegNo varchar(20),
CourseName varchar(20),
)

create table Attendance1(
StudentRegNo varchar(20),
CourseName varchar(20),
TimeStamp datetime,
Status bit,
Semester varchar(20)
)
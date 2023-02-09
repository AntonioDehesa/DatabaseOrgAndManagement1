set global local_infile = 1;

drop database if exists departmentstore;
create database departmentstore;
use departmentstore;

# this example is used for an outer joins exercise to find out:
#   a) which employees do not work for any department
#   b) which departments do not have any employees working for that department

drop table if exists WorksFor ;
drop table if exists Employee ;
drop table if exists Department ;

create table Employee (
  eid int,
  name varchar(20),
  age int,
  salary float,
  residenceState char(2),
  startDate date,
  Primary Key (eid) ) ;

create table Department (
  did int,
  name varchar(20),
  floor int,
  supplyBudget float,
  stateLocated char(2),
  PRIMARY KEY (did) ) ;

create table WorksFor (
  eid int,
  did int, 
  startDate date,
  PRIMARY KEY (did,eid),
  Foreign Key (did) references Department(did),
  Foreign Key (eid) references Employee(eid) ) ;


load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/6.1/data_emps_v3' into table Employee
  fields terminated by ','
    lines terminated by '\n'
  ;

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/6.1/data_depts_v3' into table Department
  fields terminated by ','
    lines terminated by '\n'
  ;

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/6.1/data_worksFor_v3' into table WorksFor
  fields terminated by ','
    lines terminated by '\n'
  ;
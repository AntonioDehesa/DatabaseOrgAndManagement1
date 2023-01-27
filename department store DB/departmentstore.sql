set global local_infile = 1;
  
drop table if exists worksFor;
drop table if exists manages;
drop table if exists department;
drop table if exists employee;

create table employee(
        eid int,
        name varchar(20),
        age int,
        salary float,
        residenceState varchar(20),
        Primary Key (eid));

create table Department(
        did int,
        name varchar(20),
        supplyBudget float,
        stateLocated varchar(20),
        Primary Key (did));

create table worksFor(
        eid int,
        did int,
        startDate date,
        Primary Key (eid,did,startDate),
        Foreign Key (eid) references employee (eid),
        Foreign Key (did) references department (did));

create table manages(
        eid int,
        did int,
        managesStartDate date,
        Primary Key (eid,did),
        Foreign Key (eid) references employee (eid),
        Foreign Key (did) references department (did));


load data local infile '/Users/rino2/Downloads/EmployeeData.txt' into table employee
fields terminated by ','
lines terminated by '\r';

load data local infile '/Users/rino2/Downloads/DepartmentData.txt' into table department
fields terminated by ','
lines terminated by '\r';

load data local infile '/Users/rino2/Downloads/WorksForData.txt' into table worksFor
fields terminated by ','
lines terminated by '\r';

load data local infile '/Users/rino2/Downloads/ManagesData.txt' into table manages
fields terminated by ','
lines terminated by '\r';

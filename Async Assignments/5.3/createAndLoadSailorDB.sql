set global local_infile = 1 ;

drop table if exists Reserve ;
drop table if exists Sailors ;
drop table if exists Boats ;

create table Sailors (
  sid int,
  name varchar(20) NOT NULL,
  age int,
  rating float NOT NULL,
  Primary Key (sid) ) ;

create table Boats (
  bid int,
  name varchar(20),
  ratingNeeded int,
  bcolor varchar(20),
  PRIMARY KEY (bid) ) ;

create table Reserve (
  bid int,
  sid int, 
  rdate date,
  PRIMARY KEY (bid,sid,rdate),
  Foreign Key (bid) references Boats(bid),
  Foreign Key (sid) references Sailors(sid) ) ;


load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/5.3/data_sailors' into table sailors
  fields terminated by ','
  lines terminated by '\r\n'
  ;

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/5.3/data_boats' into table boats
  fields terminated by ','
  lines terminated by '\r\n'
  ;

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Async Assignments/5.3/data_reserve' into table reserve
  fields terminated by ','
  lines terminated by '\r\n'
  ;
# SQL Basics
Structured Query Language. 
A query language used with relational databases. 

## General query form
Select select-list
From from-list
Where qualification;

* Select list: list of columns that you want. In relational algebra, its the "project". 
* From list: set of relations that you are going to be getting data from. 
* Where qualification: Conditionals. The selection operator.

So, if we have: 
Select A1,A2,...An
from r1,r2,...rm
where P

then we would be doing a Cartesian product of all the rs, then apply a set of selection P, and then, finally, project An columns. 
In relational algebra, it would look like: 
Project A1,A2,...An (select P (r1xr2x...rm))

Rm are being equijoined. 

### Example query
Select S.sname
from Sailors S
This would get the names of all sailors. 
We could also use just
select sname 
from sailors

But by adding the S, we create something called a tuple variable, which is usefull for when we have multiple variables from different sources with the same names, we can just refer first to the touple from where it comes from, and then, the variable name. 

## Keywords and actions
* distinct: allows us to find the unique values. select distinct ... from ....
* join: It would be the equivalent of doing a join in relational algebra. In this example, it would be an equijoin.
select s.sname
from sailors s, reserve r
where s.sid = r.sid and r.bid = 2;

## Performance
In the case of the tuple variable, it would start at the first of the list of all tuples, then look for the second record, and so on. If there are constraints, it would go back to the first, applies constraints, then the second, applies constraints, etc. 
Basically, a for loop. 

Therefore, a join is basically a nested loop. Performance will drop. 

We could also have a case of 3 tuples. 
select s.name
from sailors s, reserve r1, reserve r2
where (s.sid = r1.sid) and (s.sid = r2.sid)
and (r1.date = r2.date)
and (r1.bid <> r2.bid);

Find the names of sailors who have reserved two different boats on the same day. 

# MySQL basics
* --local_infile=1: allows MySQL to load local data files
* show databases: as it appears to be. By default, we will always see databases information_schema, mysql, performance_schema, sys. There are just to keep the management system and statistics, which tables exist, and which indices. 
* use <database>: With this, we select the database to query. 
* show tables: once inside a database, we can use this to show the available tables
* describe <table>: It will tell which attributes are in the table, their type, nullable or not, primary key, etc. 

Once inside the table, we can actually run queries. 
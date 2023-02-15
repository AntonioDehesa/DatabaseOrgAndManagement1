# Scripting, Variables, Procedures

## Variables
To create a variable, you use the set keyword, and @ for the name. 
example: 
set @myvar = 5;

To select it, you can just say: 
select @myvar

You can also store the output of a command into the variable: 
select count(*) from sailors into @varsailor; 

but this only stores individual values. 
If you want to store multiple values, you would have to use multiple variables: 
select * from sailors where sid = 5 into @v1, @v2, @v3, @v4

## Procedures

Just like tables, procedures stay permanently in the dataset. 
### Example of procedure: 
drop procedure if exists proc_easy1; # This one is important, as you cannot just overwrite the procedure. Youneed to delete it and recreate it.
delimiter //
create procedure proc_easy1()
begin
    select * from sailors;
    select * from blabla;
    select join blabla;
end //
delimiter;

delimiter sets everything between the chose symbol (in this case, //) as one single entity

### Invoke procedure

To invoke it, use (call proc)

## In/Out parameter

The reserved words in and out serve for parameters. in for pass by value, and out for pass by reference

### Example

delimiter //
create procedure proc_inOut(IN inBid int, out outcount int)
begin
select count(*) into outcount
from sailors s, reserve r
where r.sid = s.sid and r.bid = inBid;
end //
delimiter;

### Example calling it
set @thenum = 0; #variable for output
set @varbid = 20; #var for input
call proc_inout(@varbid, @thenum);
select @thenum as 'num res';

### Getting additional information from a procedure
If you want more information from a procedure, one way is to create a table inside the procedure, fill it with the data produced by the procedure, and then, outside the procedure, access that table. 

### Recommendations
You should always declare variables at the beginning of the procedure, with the keyword declare, which does not require setting the value. 


# Performance of Indexing

When there is a primary key, a B-tree+ is automatically built on that key. 
That way, any query using the primary key will be very fast in comparison to any other field. 

When creating a table, you can declare an index. 
## Example
create table sailors (
    sid int, 
    name varchar(20) not null,
    age int, 
    rating float not null,
    index(age),
    primary key (sid)
)

You can also use compound keys for the index, as in multiple fields. 
It is not recommended to create an index for each variable or combination, as each index consumes space, and each value you insert into the table will have to modify each index. 

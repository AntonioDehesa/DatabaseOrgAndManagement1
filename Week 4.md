# SQL Set Operators
There include: 
* Union: Used to join the results of multiple subqueries
* Intersection: As its name suggests, it gets the intersection of results of multiple subqueries
* Minus: From subquery 1, it deletes results that appear in subquery 2

# Loading and Loading Warnings

Instead of using insert to insert data in the tables, we could use load to insert a lot of information at once. 

# SQL Nested Queries

A query that uses a result from another query. 

They can be correlated or uncorrelated

## Correlated

The tuple variable from the outer query is being used in the nested query. 

### Example
select s.sid, s.name
from sailors s
where exists (
    select *
    from reserve r
    where r.sid = s.sid and r.bid=101
)

As we can see in this example, s was not defined in the inner query, so the inner query had to look for that s in the outer query. 
## Uncorrelated

The tuple variable in the outer query is not being used in the inner query. 

### Example
select * from sailors s where s.sid in (select r.sid from reserve r where r.bid = 101)

## Operator any and operator all
any returns true if any of the subquery values meet the condition, while all only returns true if all the subquery values meet the condition
The operators previous to the keywords any and all must be a standard comparison operator (=, <>, !=, >, >=, <, or <=)
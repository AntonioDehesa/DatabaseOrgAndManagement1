# Inner join, null values, outer joins

## Inner join

Basically the same as what we have been doing, except explicitly. 
We literally use the join keyword. 

### Example
Select * from sailors s inner join reserve r on s.id = r.sid

## Null Values

Null does not equal zero or empty string. it just does not have a value

Thats why when creating the table, we can specify a value or more as not null, which means these fields are required. for example, name of people. 
Primary keys cannot be null. 

## Outer join

They include tuples that do not have tuples that have a match on the join attribute.
Useful in finding out which tuples (entities) are not participating in the join (relationship) and which relationships are missing entities 
3 types: 
* left: It takes the left part of the relation, and the matching records of the right part of the relation. As in, the entire left part, and the values of the right that do not have a relation to the left will be left as null. 
* right: The opposite of the left join
* full: It will show both tables, but in those that do not have matches, it will just fill them in with nulls. 

# B-Trees

Used as an index to speed up queries. 
They are perfectly balanced trees. It could be values or pointers to values. 

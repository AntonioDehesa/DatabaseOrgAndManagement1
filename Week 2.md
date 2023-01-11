# Relational model and algebra

## Mapping from the ER model into the relational model
The relational model takes the entities and relationships and transforms them into relations. 
A relation is a set of attributes and their types. 

In the relational model, we have the concept of schema versus instance. 
### Schema
Abstract description of the database using the relational model
Although rarely, the schema can be changed, even after the table has been created.

### Instance
Particular data that is being stored in the database at that instant in time. 
The instance is constantly changing, as the data in it is constantly changing. 

### The ER model
When using the ER model, we define them: Entity (attributes). 
Example using the library example: 
* Author (ssn, name, age).
* Books (isbn, title, edition)
* Library (name, city)
* Wrote (ssn,isbn)
* Carries (name, city, isbn, numCopies)
In this case, Author and Books are entities, ssn and isbn are their keys, and Wrote is a relationship that is using both keys. 
In the case of Carries, it is a relationship with an attribue (num Copies). 
It also requires more than just the keys. As there might be a library MLK in two different cities, we need the name of the library and city, the isbn, and the num of copies. 

The keys of the relationship would be the keys of the entities it bonds, plus any required attribute of it. 

### Optimizing Model for 1:n or n:1
In general, if the relationship is 1:n or n:1, we could just add the key of one of the entities to the other entity, and so, we could delete the relationship.
Example: 
We could modify books to include the ssn from Author, as the relationship is 1:n. One author could write many books, but in this model, a book is written by only one author. 
That way, we delete the relationship Wrote. 
Similar to 1:1. 


# Five fundamental operators

## Relational algebra

Formal mathematical system that allows us to query the relational model and to ask questions about it and to get answers. 

## Five fundamental operators
* Selection: Represented by sigma. It selects tuples, or selects records from a relation that are satisfying a constraint.
* Projection: Gives you columns from a relation, because relation is just a table. A bunch of tuples. 
* Minus: Its just a minus. Set {1,2,3} minus Set{1,2} would just be Set{3}. 
* Union: Same as in math. Set{1,2,3} union Set{3,4,5} would be Set{1,2,3,4,5}
* Cartesian Product: Takes two different relations, and combines them by doing a doubly nested for loop. 

# Additional Operators
* Set intersect: Returns the intersection of two sets. Example: 
A{A,B,C} and B{C,B,D} the intersect would be B and C. But it can be done by using the five fundamentals. 
R intersect S = R - (R - S)
* Theta join: It ties together the Cartesian product with explicit join clauses. 
Example: 
This -> project sname select cnum = 321 select student.sid = enrolled.sid (student x enrolled)
is the same as -> project sname select cnum = 321 Student theta join enrolled, where theta = student.sid = enrolled.sid. 
It does not have to be equality. It just substitutes the condition. 
* Equi join: special case of the theta join. its just the theta join, but it means only equality. 
* Natural join: same as equi join, but if there are multiple attributes in common, all pairs need to be equal. 
* Division: It does not really divide anything. It determines wether something has all of. 
Example: If a student is enrolled in every class. 
 
Let R = Project sid,cnum Grades
let s = project cnum Grades
Answer = R / S


# Python Connector

Instead of using SQL scripting directly, in data science it is very common to use Python.

# Database Normalization

Redesigning your database so it has good properties

* Reduces redundancy: redundancy adds unnecessary data
* avoids update anomalies
* minimize redesign when new tables added
* reduce query complexity

Anomalies may be caused during: 
* Insert
* Delete
* Update

When you have redundancy, same data in multiple tables, you may have instances in which you add or update or delete values into one table, but not the other ones, which may create anomalies. 
Also, its better to split the data so you do not have to include the same values multiple times just to add values to one column. 


Definition of normal forms: 

1. No set values. no attribute domain has relations as elements. No table column can have tables as its values.  
2. every non-prime attribute of the relation is dependent on the whole of every candidate key. 
3. No transitive dependency: When we have two non key attributes (normal attributes), but in reality, one of them depends on the other. And all non-prime attributes depend only on the candidate keys. 

Summary (by wikipedia):
First Normal Form: Scalar columns. Columns cannot contain relations or composite values
Second Normal Form: Every non-prime attribute has a full functional dependency on a candidate key (attributes depend on the complete primary key)
Third Normal Form: Every non-trivial functional dependency either begins with a superkey or ends with a prime attribute (attributes depend only on the primary key)
BCNF: Every non-trivial functional dependency begins with a superkey. Similar to third normal form, but stricter. 


## Functional Dependency

When one attribute depends on other attribute. 

## Candidate and Super key

Candidate key is a super key, but not backwards. 
Candidate key is a super key from which you cannot remove any fields. 

A super key is basically a set of column values that together are unique, but from which you can remove a column and they would still be unique. 
A candidate key is a set of column values that together are unique, but from which you cannot remove values, because they would lose uniqueness. 


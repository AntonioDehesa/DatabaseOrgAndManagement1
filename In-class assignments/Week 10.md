Create a sailor collection populated with three sailors and a boat collection populated
with 4 boats.

Write a function that add boat reservations to sailors. The sailor object is augmented
with a reserve key that is a json object that has a {date:dateVale, boat:boat-object-id}
and make it so that each sailor has two or more reservations for boats.

1:1 - just embed on object in the other (but do in consistently) Example: embed an
address into a person object - the address is a nested json object. To do a find:
db.collection.find(“address.state”:”CO”).

1:N - instead of embedding a single address, embed a list of addresses.





1.	import empData.csv (file is attached).

mongoimport --db dbName  --collection collectionName --type=csv --file ./empData.csv –headerline

2.	Write mongo aggregates to answer this question:

Find the average salary and number of employees in each state, where the employees are all born after 1999, grouped and sorted by state, push the salaries of each state.

db.employees.aggregate([{$group: {_id:"$state", avgSalary: {$avg: "$salary"}, numInGroup:{$sum:1}}}, {$match: {birth: {$gt : 1999}}}, {$sort: {_id: 1}}])
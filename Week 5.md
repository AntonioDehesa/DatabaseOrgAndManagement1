# Aggregates
Functions that compute calculations on a set of data. 
Common aggregates are average, min, max, sum and count. 

# Aggregates with group by and having
Group by allows me to make subgroups and apply aggregates to the subgroups. And Having allows me to apply conditions to which subgroups qualify.

## Recommended order of processing
1. Create Cartesian product of all relations
2. apply where (joins and constraints)
3. Eliminate uneeded columns
4. Sort by the group by clause(s)
5. Apply the having clause (may eliminated groups)
6. Apply the selection clause and aggregates


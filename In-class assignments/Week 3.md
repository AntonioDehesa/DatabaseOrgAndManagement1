# Schema
Sailors( sid, sname, age, rating)

Boats (bid, bname, ratingNeeded, bcolor)

Reserve(sid, bid, date)

# Questions

1) Find the sid of sailors who have reserve all boats for which there has been at least one reservation.

R = project sid,bid | Reserve
S = project bid | Reserve

T = R / S

2) Find the sid of sailors who have reserved all boats

R = project sid,bid | Reserve
S = project bid | Reserve

T = R / S

3) Find the name of 18 year old sailors who have reserved all boats that have a ratingNeeded of 10

R = project sid,bid | Reserve
S = project bid | select ratingNeeded = 10| Boats

T =  R / S

U = project sname | select age = 18 | Sailors equi join T





///////////////////////
Employee( eid, name, age, salary, residenceState, startDate)

Department( did, name, floor, supplyBudget, stateLocated)

WorksFor( eid, did, startDate)

Manages( eid, did, dateStartedManaging)

## Relational algebra
Find the name of Employees who are managers

R = project eid | Manages
S = project name | Employee equi join R

Find the name of Employees who work for the “shoe” department.

Project name  Select D.name=”Shoe” E join D 

## SQL
Find the name of departments located in “CO”

SELECT Department.name
FROM Department D
WHERE D.stateLocated = "CO"

Find the name of employees who work for a department located in “CO”

SELECT E.name
FROM Employee E
INNER JOIN WorksFor WF ON WF.eid = E.eid
INNER JOIN Department D ON D.did = WF.did
WHERE D.stateLocated = "CO"

Find the name of employees  and name of department they work in  for those who work for a department that is in a different state than their residence state.

SELECT E.name AS "Employee Name", D.name AS "Department Name"
FROM Employee E
INNER JOIN WorksFor WF ON WF.eid = E.eid
INNER JOIN Department D ON D.did = WF.did
WHERE D.stateLocated != E.residenceState
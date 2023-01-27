1) Find the name of the employee who works for "department101" department.  Do this without nested queries, and using the join syntax we have used to date, i.e. (i.e. e.eid = w.eid) , not "join on..."

select e.name from employee e, worksfor wf, department d
where e.eid = wf.eid
and d.did = wf.did
and d.name = "department101"

2) Now do this with nested queries

select e.name from employee e
where e.eid in (select wf.eid from worksfor wf
where wf.did in
(select d.did from department d
where d.name = "department101"))

3) What happens if you replace the innermost "in" with "not in"?

we get the employees that do not work in department 101
-----------

4) Find the name of employees who manage department 101.  First do without nested queries (and without saying "join" in your query)

select e.name from employee e, manages m, department d
where e.eid = m.eid
and d.did = m.did
and d.name = "department101"

5) Now do with nested queries

select e.name from employee e
where e.eid in (select m.eid from manages m
where m.did in
(select d.did from department d
where d.name = "department101"))

6) what happens if you replace "in" with "not in"

we get the other managers that do not manage department 101



#### ACT TWO

1) Find all information about employees who work for department 101 using correlated nested queries (i.e. exists)

select e.eid, e.name, e.age, e.salary, e.residenceState from employee e
where exists (select wf.eid from worksfor wf where exists( select d.did from department d where d.did = wf.did and e.eid = wf.eid and d.name = "department101"))

2) Find the number of employees that work for department 101 using correlated nested queries.  Hint:  select count (*) from...

select count(*) from employee e
where exists (select wf.eid from worksfor wf where exists( select d.did from department d where d.did = wf.did and e.eid = wf.eid and d.name = "department101"))

3) Find the number of employees that do NOT work for department 101 using correlated nested queries

select count(*) from employee e
where exists (select wf.eid from worksfor wf where exists( select d.did from department d where d.did = wf.did and e.eid = wf.eid and d.name <> "department101"))

4) Find the employee who lives in a state by her\himself (i.e. no other employees live in the same state)

select *

from employee e

where e.residenceState not in (

  select e2.residenceState

  from employee e2

  where e.eid <> e2.eid ) ;

5) Find the department(s) with the largest supplyBudget (do not use MAX aggregate, use any/all ops)
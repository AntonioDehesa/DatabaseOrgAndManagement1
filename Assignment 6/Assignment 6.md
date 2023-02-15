#Q1: Find all information about managers who are 25 years old or younger and live in California (‘CA’).
select m.* from manages as m join  employee as e on e.eid = m.eid
where e.age <= 25
and e.residencestate = "CA";

#Q2: Find the name, salary, age, and residence state of all 20-year-old or younger managers who live in Indiana (‘IN’).
select e.name, e.salary, e.age, e.residencestate from manages as m join  employee as e on e.eid = m.eid
where e.age <= 20
and e.residencestate = "IN";

no result

#Q3: Find the names and salary of 25-year-old employees who work for departments located on the fourth floor in Alaska (‘AK’).
select e.name, e.salary from employee e join worksfor as wf on (wf.eid = e.eid) join department as d on (d.did = wf.did)
where e.age = 25
and e.residencestate = "AK"
and
d.floor = 4;


#Q4: Find the name, salary, and EID of 49-year-old employees who work for a department located in Alaska (‘AK’) but live in California (‘CA’).
select e.name, e.salary, e.eid from employee e join worksfor as wf on (wf.eid = e.eid) join department as d on (d.did = wf.did)
where e.age = 49
and
d.statelocated = "AK"
and e.residencestate = "CA";



#Q5: Find the total number of employees.
select count(distinct eid) from employee;


#Q6: Find the number of employees who are managers.
select count(distinct eid) from manages;

#Q7: Find the number of employees who are not managers.
select count(distinct e.eid) from employee e
where e.eid not in (select m.eid from manages m);


#Q8: Find the (eid,number) pair for employees who are managing two or more departments where "number" is the number of departments they are managing.
select m.eid, count(distinct m.did) as number_dep from manages m
group by m.eid
having number_dep >= 2
order by number_dep desc;


#Q9: Present the (name1, salary1, name2, salary2), where salary1 is the salary of the employee with name1 and salary2 corresponds with name2, of all employee pairs where both are living in California (‘CA’), one is a 24-year-old manager, the other (who can be any age) is not a manager, and the manager earns more than three times the other employee.

with managers as (select m.eid as eid1, e.name as name1, e.salary as salary1, m.did from manages as m join employee as e on (m.eid = e.eid) where e.age = 24 and e.residencestate = "CA"),
employees as (select e.eid as eid2, e.name as name2, e.salary as salary2, wf.did from employee as e join worksfor wf on (wf.eid = e.eid) where e.residencestate = "CA")
select m.name1, m.salary1, e.name2, e.salary2 from managers as m join employees as e on (m.did = e.did)
where m.salary1 > 3*e.salary2
order by name1;

It returns nothing, as there are no managers in CA that are exactly 24 YO



#Q10: For each department in Alaska ('AK') that has 25 or more employees working for it and a supply budget < $7,000, present the did, budget, and number of employees that work in that department.
select d.did, d.supplybudget, count(distinct wf.eid) as num_employees from department as d join worksfor as wf on (d.did = wf.did)
where d.supplybudget < 7000
and
d.statelocated = "AK"
group by d.did
having num_employees >= 25;



#Q11: For each state, present the salary of the average 20-year-old manager (i.e., average salary of mangers who are 20 years old) who lives in that state 
#and the number of such managers. Note: Your results can omit states that do not have any 20-year-old managers living in them.
select e.residencestate, avg(e.salary) from manages as m join employee as e on (m.eid = e.eid)
where e.age = 20
group by e.residencestate;
Answer the following null value queries:

   1. Which employees do not have a known residenceState?  
   2. Which departments do not have a known supplyBudget?


Use outer joins to answer the two following queries:

    1. Which employees do not work in any department?
    2. Which departments have no employees working for them?




answers

select * from employee where residencestate is null;

select * from department where supplybudget is null;

select e.name from employee e left outer join worksfor wf on e.eid = wf.eid
where wf.did is null;

select d.name from department d left outer join worksfor wf on d.did = wf.did
where wf.eid is null;


create a b tree with:
50, 100, 20, 150, 125, 30, 25

M = 2


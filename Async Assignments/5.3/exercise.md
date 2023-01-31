Q1: Find all attributes/fields of each 18-year-old sailor whose rating is greater than 9.

select s.* from sailors s
where s.rating > 9;

Q2: Find the first reservation (i.e., lowest rdate) for each sailor with ids less than 5.

select s.sid, min(r.rdate) from sailors s, reserve r
where s.sid = r.sid
and 
s.sid < 5
group by s.sid;

Q3: Find the number of reservations by 18-year-old sailors.

select s.sid, count(r.rdate) from sailors s, reserve r
where s.sid = r.sid
and 
s.age = 18
group by s.sid;

Q4: Find the sailor name, age, and boat name for all reservations on 2019-01-23 made by sailors who are 40 years old or older. Show the results sorted by age.

select s.name as sailor_name, s.age, b.name as boat_name from sailors s, boats b, reserve r
where s.sid = r.sid
and
b.bid = r.bid
and
s.age >= 40
order by s.age;

Q5: Find all attributes/fields of boats that are "pumpkin" color and have a ratingNeeded that is the maximum of all ratingNeeded for all boats.

select b.* from boats b
where b.bcolor = "pumpkin"
and b.ratingNeeded = (select max(ratingNeeded) from boats);

Q6: Find the name, rating, ratingNeeded, and bid of all reservations by 18-year-old sailors that have reserved a boat for which there rating is less than the rating needed. Sort the results by sid.

select s.name, s.rating, b.ratingNeeded  from sailors s, reserve r, boats b
where s.sid = r.sid
and b.bid = r.bid
and
s.age = 18
and
s.rating < b.ratingNeeded
order by s.sid;

Q7: For each 18-year-old sailor who has reserved one or more boats where the ratingNeeded is > than their rating, return sid of each such sailor and the number of these reservations. Order by sid.

select s.sid, count(*)  from sailors s, reserve r, boats b
where s.sid = r.sid
and b.bid = r.bid
and
s.age = 18
and
s.rating < b.ratingNeeded
group by s.sid;

Q8: Find average rating for each age group of sailors who are 31...39 years old, inclusive.

select s.age, avg(s.rating) from sailors s
where s.age >= 31
and s.age <= 39
group by s.age
order by s.age;

Q9: Find average rating for each age group of sailors who are 31...39 years old, but only include groups that have 30 or more sailors of that age.

with sailors_age_group as (select s.age, count(*) as total_sailors_by_age_group from sailors s where s.age >= 31 and s.age <= 39 group by s.age having total_sailors_by_age_group > 30)
select s.age, avg(s.rating) from sailors s
where s.age in (select age from sailors_age_group)
group by s.age;

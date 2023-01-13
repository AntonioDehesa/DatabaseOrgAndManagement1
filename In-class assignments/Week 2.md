Schema: 

Sailors( sid, sname, age, rating)

Boats (bid, bname, ratingNeeded, bcolor)

Reserve(sid, bid, date)

S = Sailors
B = Boats
R = Reserve

Assuming the Sailor DB schema, using ONLY the 5 fundamental operators, {project, select, cartesian product, union, minus}, in your breakout group, answer the following RA questions:
1) Find the name of sailors who have reserved one or more boats on 2020-07-04

R1 = Reserve
R2 = Reserve

project sname | select r1.bid != r2.bid | select r1.dat = r2.date | (S equi R1 equi R2)

2) Find the name and age of sailors who have reserve boat number 101 (i.e. bid == 101)

project name, age | select bid = 101 | ( S equi R )

3) Find the name and age of sailors who have reserved a ‘red’ boat

Someone else on the team did this one

4) Find the name and age of sailors who have reserved a boat for which their rating is too low.

project sname, age | select s.raiting < b.ratingNeeded | ( s equi r equi b)

5) Find the name of boats reserved by 18 year old sailors



6) Find the dates of reservations by sailor “Scott” for ‘green’ boats



7) Find the sid,sname of sailors who have reserved at least one ‘red’ boat but no ‘green’ boats.
project sid,sname, select b.color = red, select bcolor != green, select s.sid = r.sid, select r.bid = b.bid, rxsxb
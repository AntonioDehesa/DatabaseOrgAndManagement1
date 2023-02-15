# 1 
## Insert statement
insert into played(Title, played_times)
values ("Game that definitely does not exist", 5);

## Response
ERROR: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`games`.`played`, CONSTRAINT `played_ibfk_1` FOREIGN KEY (`Title`) REFERENCES `games` (`Title`))

## update statement 1

 MySQL  localhost:3306 ssl  games  SQL > update played set title = "Game that definitely does not exist" where played_times = 434;
Query OK, 0 rows affected (0.0307 sec)

Rows matched: 0  Changed: 0  Warnings: 0

We can see that if no value matches the where condition, it does not check for the foreign key constraint
## update statement 2
but if there are values that match the where condition, the constraint is checked.

 MySQL  localhost:3306 ssl  games  SQL > update played set title = "Game that definitely does not exist" where played_times = 5;
ERROR: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`games`.`played`, CONSTRAINT `played_ibfk_1` FOREIGN KEY (`Title`) REFERENCES `games` (`Title`))
 MySQL  localhost:3306 ssl  games  SQL >

# 2
## Procedure

delimiter //
create procedure proc_get_median_game_date_per_console(IN Console varchar(20), out median_date date)
begin
select date(from_unixtime(avg( unix_timestamp(g.release_date)))) into median_date from games g, ownedon oo
where g.title = oo.title
and
oo.sname = Console;
end //
delimiter ;

## Response
set @console="PlayStation 3";
Query OK, 0 rows affected (0.0070 sec)
 MySQL  localhost:3306 ssl  games  SQL > set @avg_date;
ERROR: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
 MySQL  localhost:3306 ssl  games  SQL > set @avg_date=0;
Query OK, 0 rows affected (0.0002 sec)
 MySQL  localhost:3306 ssl  games  SQL > call proc_get_median_game_date_per_console(@console, @avg_date)
                                      -> ;
Query OK, 1 row affected (0.0253 sec)
 MySQL  localhost:3306 ssl  games  SQL > select @avg_date;
+------------+
| @avg_date  |
+------------+
| 1996-08-04 |
+------------+

## Explanation
This procedure will give us the average release date for the games in a console. The input for this procedure is the console for which we want to get the average release date of its games. 
The output is simply the average release date for the games in that console. 

# 3
## No Index
In this case, I have no index created for release_date
### Single relation

 MySQL  localhost:3306 ssl  games  SQL > select * from games
                                      -> where release_date = "1978-07-15";
+------------------------------------+--------------+---------------------+----------------+-----------------+
| Title                              | release_date | developer           | classification | Genre           |
+------------------------------------+--------------+---------------------+----------------+-----------------+
| Ace Attorney: Back to Karkand      | 1978-07-15   | Epic Games          | E+10           | Life simulation |
| Ghosts 'n Goblins: Madness Returns | 1978-07-15   | Santa Monica Studio | M              | Strategy        |
| Math Blaster: 2 Fast 2 Furious     | 1978-07-15   | Bungie Inc          | A              | Stealth         |
| The Walking Dead: Madness Returns  | 1978-07-15   | Ubisoft             | E              | Beat 'em up     |
+------------------------------------+--------------+---------------------+----------------+-----------------+
4 rows in set (0.0158 sec)

### Join

 MySQL  localhost:3306 ssl  games  SQL > select * from games g, partof po
                                      -> where g.release_date = "1978-07-15"
                                      -> and g.title = po.title;
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
| Title                              | release_date | developer           | classification | Genre           | Saga              | Title                              |
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
| Ace Attorney: Back to Karkand      | 1978-07-15   | Epic Games          | E+10           | Life simulation | Ace Attorney      | Ace Attorney: Back to Karkand      |
| Ghosts 'n Goblins: Madness Returns | 1978-07-15   | Santa Monica Studio | M              | Strategy        | Ghosts 'n Goblins | Ghosts 'n Goblins: Madness Returns |
| Math Blaster: 2 Fast 2 Furious     | 1978-07-15   | Bungie Inc          | A              | Stealth         | Math Blaster      | Math Blaster: 2 Fast 2 Furious     |
| The Walking Dead: Madness Returns  | 1978-07-15   | Ubisoft             | E              | Beat 'em up     | The Walking Dead  | The Walking Dead: Madness Returns  |
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
4 rows in set (0.0155 sec)
 MySQL  localhost:3306 ssl  games  SQL >

## Index

In this case, release_date has an index.
 MySQL  localhost:3306 ssl  games  SQL > create index idx_release_date on games(release_date);
Query OK, 0 rows affected (0.1123 sec)

### Single relation

select * from games where release_date = "1978-07-15";
+------------------------------------+--------------+---------------------+----------------+-----------------+
| Title                              | release_date | developer           | classification | Genre           |
+------------------------------------+--------------+---------------------+----------------+-----------------+
| Ace Attorney: Back to Karkand      | 1978-07-15   | Epic Games          | E+10           | Life simulation |
| Ghosts 'n Goblins: Madness Returns | 1978-07-15   | Santa Monica Studio | M              | Strategy        |
| Math Blaster: 2 Fast 2 Furious     | 1978-07-15   | Bungie Inc          | A              | Stealth         |
| The Walking Dead: Madness Returns  | 1978-07-15   | Ubisoft             | E              | Beat 'em up     |
+------------------------------------+--------------+---------------------+----------------+-----------------+
4 rows in set (0.0074 sec)

### Join

 MySQL  localhost:3306 ssl  games  SQL > select * from games g, partof po where g.release_date = "1978-07-15" and g.title = po.title;
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
| Title                              | release_date | developer           | classification | Genre           | Saga              | Title                              |
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
| Ace Attorney: Back to Karkand      | 1978-07-15   | Epic Games          | E+10           | Life simulation | Ace Attorney      | Ace Attorney: Back to Karkand      |
| Ghosts 'n Goblins: Madness Returns | 1978-07-15   | Santa Monica Studio | M              | Strategy        | Ghosts 'n Goblins | Ghosts 'n Goblins: Madness Returns |
| Math Blaster: 2 Fast 2 Furious     | 1978-07-15   | Bungie Inc          | A              | Stealth         | Math Blaster      | Math Blaster: 2 Fast 2 Furious     |
| The Walking Dead: Madness Returns  | 1978-07-15   | Ubisoft             | E              | Beat 'em up     | The Walking Dead  | The Walking Dead: Madness Returns  |
+------------------------------------+--------------+---------------------+----------------+-----------------+-------------------+------------------------------------+
4 rows in set (0.0012 sec)



We can see that with the index, the execution time was cut in half for the single relation, 
while for the join it was only 1/10 of the original execution time. 
This is with over 40000 rows.
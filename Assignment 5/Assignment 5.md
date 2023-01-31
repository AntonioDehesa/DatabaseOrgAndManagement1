# Queries
For each, no more than 20 tuples.
## One must involve a two-way or three-way join with a where clause that limits the results to 20 of fewer tuples.

select g.title, e.global_score, s.saga, a.systemname from availability a, games g, enjoyment e, saga s
where e.global_score = 10
and
g.title = e.Game
and
g.title = s.members
and
a.SagaName = s.saga
and
a.systemname = "Wii"

### Result

 MySQL  localhost:3306 ssl  games  SQL > select g.title, e.global_score, s.saga, a.systemname from availability a, games g, enjoyment e, saga s
                                      -> where e.global_score = 10
                                      -> and
                                      -> g.title = e.Game
                                      -> and
                                      -> g.title = s.members
                                      -> and
                                      -> a.SagaName = s.saga
                                      -> and
                                      -> a.systemname = "Wii";
+------------------------+--------------+--------------+------------+
| title                  | global_score | saga         | systemname |
+------------------------+--------------+--------------+------------+
| Herzog: II             |           10 | Herzog       | Wii        |
| Iron Soldier: Valhalla |           10 | Iron Soldier | Wii        |
+------------------------+--------------+--------------+------------+
2 rows in set (0.0097 sec)

### Explanation
Find all the games that have a perfect score, show the sagas to which they belong, their perfect score, but only those that are available for the Wii console. 

## One must be an aggregate using a group by clause.

select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s
where p.title = s.members
and s.saga like "%shock%"
group by s.saga
order by total_played_times_saga desc

### Result

 MySQL  localhost:3306 ssl  games  SQL > select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s
                                      -> where p.title = s.members
                                      -> and s.saga like "%shock%"
                                      -> group by s.saga
                                      -> order by total_played_times_saga desc;
+--------------+-------------------------+
| saga         | total_played_times_saga |
+--------------+-------------------------+
| System Shock |                     433 |
| BioShock     |                     414 |
+--------------+-------------------------+
2 rows in set (0.0131 sec)

### Explanation
query to find from which saga, systemshock or bioshock, I have played its games more times

## One must be an aggregate using a group by clause and a having clause. 

select s.saga, avg(e.global_score) as average_score from saga s, enjoyment e
where s.members = e.game
group by s.saga
having average_score > 5.6
order by average_score desc

### Result

 MySQL  localhost:3306 ssl  games  SQL > select s.saga, avg(e.global_score) as average_score from saga s, enjoyment e
                                      -> where s.members = e.game
                                      -> group by s.saga
                                      -> having average_score > 5.6
                                      -> order by average_score desc;
+-------------------------+---------------+
| saga                    | average_score |
+-------------------------+---------------+
| Rolling Thunder         |        5.8500 |
| Backyard Sports         |        5.7750 |
| Kane & Lynch            |        5.7750 |
| Alien Syndrome          |        5.7500 |
| Qix                     |        5.7500 |
| Audiosurf               |        5.7000 |
| Nidhogg                 |        5.6750 |
| Soldier of Fortune      |        5.6750 |
| Iron Soldier            |        5.6500 |
| Lemmings                |        5.6500 |
| Vampire: The Masquerade |        5.6500 |
| 1942                    |        5.6250 |
| Puzzle League           |        5.6250 |
| Wangan Midnight         |        5.6250 |
+-------------------------+---------------+
14 rows in set (0.0513 sec)

### Explanation 
Show the sagas of games that have an average score from all their games being over 5.6, in a descendent order. 

# Updates to the db

## One should be a simple insert

### Before

 MySQL  localhost:3306 ssl  games  SQL > select g.title, e.global_score
                                      -> from games g, enjoyment e
                                      -> where g.title = e.Game
                                      -> and g.title like "%Horizon%";
+----------------------------+--------------+
| title                      | global_score |
+----------------------------+--------------+
| Horizon: 1942              |            5 |
| Horizon: 2                 |            4 |
| Horizon: 2 Fast 2 Furious  |            4 |
| Horizon: 3                 |            6 |
| Horizon: 4                 |            3 |
| Horizon: 5                 |            5 |
| Horizon: 6                 |            5 |
| Horizon: Advanced Warfare  |            7 |
| Horizon: Armored Fury      |            5 |
| Horizon: Ascension         |            5 |
| Horizon: Back to Karkand   |            6 |
| Horizon: Bad Company       |            7 |
| Horizon: Black Flag        |            7 |
| Horizon: Black Ops         |            5 |
| Horizon: Brotherhood       |            5 |
| Horizon: Chains of Olympus |            4 |
| Horizon: Electric Boogaloo |            5 |
| Horizon: Forbidden West    |            6 |
| Horizon: Ghost of Sparta   |            6 |
| Horizon: Ghosts            |            6 |
| Horizon: Hardline          |            5 |
| Horizon: Heroes            |            6 |
| Horizon: I                 |            9 |
| Horizon: II                |            6 |
| Horizon: III               |            7 |
| Horizon: Infinity          |            4 |
| Horizon: Isolation         |            6 |
| Horizon: Madness Returns   |            5 |
| Horizon: Modern Combat     |            6 |
| Horizon: Modern Warfare    |            8 |
| Horizon: Odyssey           |            7 |
| Horizon: Origins           |            5 |
| Horizon: Revelations       |            5 |
| Horizon: Rogue             |            8 |
| Horizon: Syndicate         |            5 |
| Horizon: Tokyo Drift       |            5 |
| Horizon: Valhalla          |            5 |
| Horizon: Vietnam           |            6 |
| Horizon: World at War      |            3 |
| Horizon: Zero Dawn         |            6 |
+----------------------------+--------------+
40 rows in set (0.0148 sec)

### Insert statement

 MySQL  localhost:3306 ssl  games  SQL > insert into games(title, release_date, developer, classification, genre) values ("Horizon: Burning Shores", "2023-05-28", "Guerrilla", "T", "Action");
Query OK, 1 row affected (0.0078 sec)
 MySQL  localhost:3306 ssl  games  SQL >
 MySQL  localhost:3306 ssl  games  SQL > insert into enjoyment(Game,  music_score, graphics_score,  gameplay_score, story_score,global_score)
                                      -> values ("Horizon: Burning Shores",10,10,10,10,10);
Query OK, 1 row affected (0.0077 sec)

### After

 MySQL  localhost:3306 ssl  games  SQL > select g.title, e.global_score  from games g, enjoyment e where g.title = e.Game  and g.title like "%Horizon%";
+----------------------------+--------------+
| title                      | global_score |
+----------------------------+--------------+
| Horizon: 1942              |            5 |
| Horizon: 2                 |            4 |
| Horizon: 2 Fast 2 Furious  |            4 |
| Horizon: 3                 |            6 |
| Horizon: 4                 |            3 |
| Horizon: 5                 |            5 |
| Horizon: 6                 |            5 |
| Horizon: Advanced Warfare  |            7 |
| Horizon: Armored Fury      |            5 |
| Horizon: Ascension         |            5 |
| Horizon: Back to Karkand   |            6 |
| Horizon: Bad Company       |            7 |
| Horizon: Black Flag        |            7 |
| Horizon: Black Ops         |            5 |
| Horizon: Brotherhood       |            5 |
| Horizon: Burning Shores    |           10 |
| Horizon: Chains of Olympus |            4 |
| Horizon: Electric Boogaloo |            5 |
| Horizon: Forbidden West    |            6 |
| Horizon: Ghost of Sparta   |            6 |
| Horizon: Ghosts            |            6 |
| Horizon: Hardline          |            5 |
| Horizon: Heroes            |            6 |
| Horizon: I                 |            9 |
| Horizon: II                |            6 |
| Horizon: III               |            7 |
| Horizon: Infinity          |            4 |
| Horizon: Isolation         |            6 |
| Horizon: Madness Returns   |            5 |
| Horizon: Modern Combat     |            6 |
| Horizon: Modern Warfare    |            8 |
| Horizon: Odyssey           |            7 |
| Horizon: Origins           |            5 |
| Horizon: Revelations       |            5 |
| Horizon: Rogue             |            8 |
| Horizon: Syndicate         |            5 |
| Horizon: Tokyo Drift       |            5 |
| Horizon: Valhalla          |            5 |
| Horizon: Vietnam           |            6 |
| Horizon: World at War      |            3 |
| Horizon: Zero Dawn         |            6 |
+----------------------------+--------------+
41 rows in set (0.0148 sec)

## one a simple update 

### Before

 MySQL  localhost:3306 ssl  games  SQL > select distinct s.saga, s.total_games from saga s
                                      -> order by s.Saga
                                      -> limit 10;
+--------------------+-------------+
| saga               | total_games |
+--------------------+-------------+
| .hack              |          40 |
| 'Splosion Man      |          40 |
| 1080° Snowboarding |          40 |
| 1942               |          40 |
| 3-D Ultra Pinball  |          40 |
| 3D Ultra Minigolf  |          40 |
| 7th Dragon         |          40 |
| A Boy and His Blob |          40 |
| Ace Attorney       |          40 |
| Ace Combat         |          40 |
+--------------------+-------------+
10 rows in set (0.0008 sec)

### Statement

update saga
set saga.total_games = 55
where saga.Saga = "A Boy and His Blob";

### After

 MySQL  localhost:3306 ssl  games  SQL > select distinct s.saga, s.total_games from saga s
                                      -> order by s.Saga
                                      -> limit 10
                                      -> ;
+--------------------+-------------+
| saga               | total_games |
+--------------------+-------------+
| .hack              |          40 |
| 'Splosion Man      |          40 |
| 1080° Snowboarding |          40 |
| 1942               |          40 |
| 3-D Ultra Pinball  |          40 |
| 3D Ultra Minigolf  |          40 |
| 7th Dragon         |          40 |
| A Boy and His Blob |          55 |
| Ace Attorney       |          40 |
| Ace Combat         |          40 |
+--------------------+-------------+
10 rows in set (0.0006 sec)

## one an update that updates several tuples at once. 

### Before

 MySQL  localhost:3306 ssl  games  SQL > select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s
                                      -> where p.title = s.members
                                      -> and s.saga like "%shock%"
                                      -> group by s.saga
                                      -> order by total_played_times_saga desc;
+--------------+-------------------------+
| saga         | total_played_times_saga |
+--------------+-------------------------+
| System Shock |                     433 |
| BioShock     |                     414 |
+--------------+-------------------------+
2 rows in set (0.0132 sec)

### Statement

UPDATE played
        INNER JOIN
    games ON games.title = played.title 
    inner join
    saga on games.title = saga.members
SET 
    played_times = 40
    where saga.Saga like "%bioshock%";

### After

 MySQL  localhost:3306 ssl  games  SQL > select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s where p.title = s.members and s.saga like "%shock%" group by s.saga order by total_played_times_saga desc;
+--------------+-------------------------+
| saga         | total_played_times_saga |
+--------------+-------------------------+
| BioShock     |                    1600 |
| System Shock |                     433 |
+--------------+-------------------------+
2 rows in set (0.0130 sec)


In this one, it updates the played times for all the games in the "Bioshock" saga

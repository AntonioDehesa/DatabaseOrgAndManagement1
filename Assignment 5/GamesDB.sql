# First, we create the database, the tables, and load the data for the tests
drop database if exists games2;
create database games2;
use games2;
set global local_infile = 1;
  
drop table if exists OwnedOn;
drop table if exists Played;
drop table if exists PartOf;
drop table if exists Availability;
drop table if exists Game_system;
drop table if exists Enjoyment;
drop table if exists Saga;
drop table if exists Games;

# Entities
CREATE TABLE if not exists Games (     
			Title varchar(255) primary key,     
            release_date date,     
            developer varchar(255),     
            classification varchar(255),     
            Genre varchar(255) );
            
CREATE TABLE if not exists game_system (     
			sName varchar(255) primary key,     
            release_date date,     
            Company varchar(255),     
            sstatus varchar(255),     
            owned_copies int );
            
            
CREATE TABLE if not exists enjoyment (     
			Game varchar(255) primary key,     
            music_score int not null,    
            graphics_score int not null,     
            gameplay_score int not null,     
            story_score int not null,
            global_score int not null,     
            foreign key (Game) references Games(Title) );
            
            
CREATE TABLE if not exists saga (     
			Saga varchar(255) not null,     
            total_games int not null,     
            members varchar(255) not null,  
            foreign key (members) references Games(Title),
            primary key (Saga,members) );

# Relationships
CREATE TABLE if not exists ownedOn (     
			Title varchar(255) not null,
            sName varchar(255) not null,
            foreign key (Title) references Games(Title),
            foreign key (sName) references game_system(sName),
            primary key (Title) );
            
create table if not exists played(
			Title varchar(255) primary key,
            played_times int not null,
            foreign key (Title) references Games(Title)
);

create table if not exists partOf(
			Saga varchar(255) not null,
            Title varchar(255) not null,
            foreign key (Saga) references Saga(Saga),
            foreign key (Title) references Games(Title),
            primary key (Title)
);

create table if not exists availability(
			SystemName varchar(255) not null,
            SagaName varchar(255) not null,
            foreign key (SagaName) references Saga(Saga),
            foreign key (SystemName) references game_system(sName)
);

# Loading data

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Games' into table games
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Game_System' into table game_system
fields terminated by '|'
lines terminated by '\r\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Enjoyment' into table enjoyment
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Saga' into table saga
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/OwnedOn' into table ownedon
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Played' into table played
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/PartOf' into table partof
fields terminated by '|'
lines terminated by '\n';

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Database Organization and Management 1/DatabaseOrgAndManagement1/Assignment 5/Availability' into table availability
fields terminated by '|'
lines terminated by '\n';

# Now, we can show assignment 5
# Queries
## For each, no more than 20 tuples.
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
a.systemname = "Wii";

### Explanation
#Find all the games that have a perfect score, show the sagas to which they belong, their perfect score, but only those that are available for the Wii console. 

## One must be an aggregate using a group by clause.

select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s
where p.title = s.members
and s.saga like "%shock%"
group by s.saga
order by total_played_times_saga desc;

### Explanation
# query to find from which saga, systemshock or bioshock, I have played its games more times

## One must be an aggregate using a group by clause and a having clause. 

select s.saga, avg(e.global_score) as average_score from saga s, enjoyment e
where s.members = e.game
group by s.saga
having average_score > 5.6
order by average_score desc;

### Explanation 
# Show the sagas of games that have an average score from all their games being over 5.6, in a descendent order. 

# Updates to the db

## One should be a simple insert
### Before
select g.title, e.global_score from games g, enjoyment e where g.title = e.Game and g.title like "%Horizon%";
### Statement
insert into games(title, release_date, developer, classification, genre) values ("Horizon: Burning Shores", "2023-05-28", "Guerrilla", "T", "Action");
insert into enjoyment(Game,  music_score, graphics_score,  gameplay_score, story_score,global_score) values ("Horizon: Burning Shores",10,10,10,10,10);

### After
select g.title, e.global_score from games g, enjoyment e where g.title = e.Game and g.title like "%Horizon%";

## one a simple update 

### Before
select distinct s.saga, s.total_games from saga s order by s.Saga limit 10;
### Statement

update saga
set saga.total_games = 55
where saga.Saga = "A Boy and His Blob";

### After
select distinct s.saga, s.total_games from saga s order by s.Saga limit 10;

## one an update that updates several tuples at once. 

### Before
select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s where p.title = s.members and s.saga like "%shock%" group by s.saga order by total_played_times_saga desc;

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
select s.saga, sum(p.played_times) as total_played_times_saga from played p, saga s where p.title = s.members and s.saga like "%shock%" group by s.saga order by total_played_times_saga desc;
# In this one, it updates the played times for all the games in the "Bioshock" saga
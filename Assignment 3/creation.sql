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
            played_times int not null,
            global_score int not null,     
            foreign key (Game) references Games(Title) );
            
            
CREATE TABLE if not exists saga (     
			Saga varchar(255) not null,     
            total_games int not null,     
            members varchar(255) not null,     
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
            foreign key (SystemName) references game_system(sName),
            primary key(SagaName)
);
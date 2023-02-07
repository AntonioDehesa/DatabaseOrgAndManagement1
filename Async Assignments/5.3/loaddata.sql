set global local_infile = 1;
  
drop table if exists accidents;
drop table if exists prices;
# Entities
CREATE TABLE if not exists accidents (
			state int not null,
			state_name varchar(255) not null,    
            st_case int not null,
            veh_no int not null,
            ve_forms int not null,
            numoccs int not null,
            numoccsname varchar(255) not null, 
            day int not null,
            month int not null,
            hour int not null,
            minute int not null,
            harm_ev int not null,
            harm_evname varchar(255) not null,
            man_coll int not null,
            man_collname varchar(255) not null,
            unittype int not null,
            unittypename varchar(255) not null,
            hit_run int not null,
            hit_runname varchar(255) not null,
            reg_stat int not null,
            reg_stat_name varchar(255),
            owner int not null,
            ownername varchar(255),
            make int not null,
            makename varchar(255) not null,
            model int not null,
            mak_mod int not null,
            mak_modname varchar(255) not null,
            body_type int not null,
            body_typename varchar(255) not null,
            mod_year int not null
            );

create table if not exists prices(
		price int not null,
        brand varchar(255) not null,
        model varchar(255) not null,
        year int not null,
        title_status varchar(255) not null,
        mileage int not null,
        color varchar(255) not null,
        vin varchar(255) not null,
        lot int not null,
        state varchar(255) not null,
        full_model varchar(255) not null
);

# Loading data

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Probability and Statistics 1/ProbAndStat1/Final/Data/clean/vehicle.csv' into table accidents
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

load data local infile '/Users/rino2/OneDrive/Documentos/Maestria/Second Quarter - Winter 2023/Probability and Statistics 1/ProbAndStat1/Final/Data/clean/prices.csv' into table prices
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# modify
set sql_safe_updates = 0;
update accidents
set mak_modname = "Mazda 323/GLC/ Protege/ Protege5"
where mak_modname = "Mazda 323/GLC/ Prot"
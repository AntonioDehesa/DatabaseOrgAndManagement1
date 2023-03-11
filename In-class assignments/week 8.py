import mysql.connector

config = {
	'user':'test',    # could be root, or a user you created, I created 'testuser'
  'password':'none',  # the password for that use
  'database':'games',   # the database to connect to
  'host':'MY IP',   # localhost
  'allow_local_infile':True  # needed so can load local files
}

mydb = mysql.connector.connect(
  **config
)
myc = mydb.cursor()   # myc name short for "my cursor"

# We need to reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 


# Create the database if it does not exist
myc.execute("drop database if exists departmentstore;")
myc.execute("create database departmentstore;")
myc.execute("use departmentstore;")
myc.execute("drop table if exists WorksFor ;")
myc.execute("drop table if exists Employee ;")
myc.execute("drop table if exists Manages ;")

# Create the tables
myc.execute("""
create table Employee (
  eid int,
  name varchar(20),
  age int,
  salary float,
  residenceState char(2),
  startDate date,
  Primary Key (eid) ) ;
  """)
myc.execute("""
create table Department (
  did int,
  name varchar(20),
  supplyBudget float,
  stateLocated char(2),
  city varchar(255),
  PRIMARY KEY (did) ) ;
""")
myc.execute("""
create table Manages (
  eid int,
  did int, 
  departmentbudget int,
  startDate date,
  PRIMARY KEY (did,eid),
  Foreign Key (did) references Department(did),
  Foreign Key (eid) references Employee(eid) ) ;
""")

mydb.commit()


# Now we add the 4-8 tuples for each table.

myc.execute("""insert into Employee values (1,\"Bob\", 25, 25000, \"CO\",
             \"2020-02-12\"), (2, \"Ana\", 42, 80000, \"CA\", \"2020-02-12\"), 
             (3, \"Ryan\", 82, 60000, \"CO\", \"2020-02-12\"), 
             (4,\"John\", 37, 45000, \"OH\", \"2020-02-12\")""")
myc.execute(""" insert into Department values (1,\"department1\",6205,\"AL\", \"some\"),
            (2,\"department2\",5419,\"CO\", \"other\"), (3,\"department3\",7984,\"AZ\", \"yeah\"), 
            (4,\"department4\",6195,\"AZ\", \"oh wow\"), (5,\"department5\",6820,\"AL\", \"very city\")
            """)
myc.execute("""insert into manages values (1,1,200000,\"2020-02-12\"), 
            (2,2,300000,\"2020-02-12\"), (3,3,400000,\"2020-02-12\"), 
            (4,4,500000,\"2020-02-12\")""")
mydb.commit()


# Now, we show all managers for deparments in CO
myc.execute("""select e.* from manages m, department d, employee e
where d.statelocated = "CO"
and 
m.eid = e.eid
and m.did = d.did""")

for x in myc.fetchall():
    print(x)

# Now we increase all salary employess from CO

mydb.close() 

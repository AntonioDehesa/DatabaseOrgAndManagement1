# first need to make sure connector is installed:
#  python3 -m pip install mysql-connector-python

import mysql.connector

# note:  look at at end of this file - mydb.commit() and mydb.close() -> do not forget
# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )

print ("Hello - starting createAndLoadSailorDB.py")

config = {
	'user':'test',    # could be root, or a user you created, I created 'testuser'
  'password':'none',  # the password for that use
  'database':'games',   # the database to connect to
  'host':'192.168.1.128',   # localhost
  'allow_local_infile':True  # needed so can load local files
}

mydb = mysql.connector.connect(
  **config
)



print(mydb)
myc = mydb.cursor()   # myc name short for "my cursor"

# We need to reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
for x in myc:
	print(x) 

mydb.commit()
mydb.close() 

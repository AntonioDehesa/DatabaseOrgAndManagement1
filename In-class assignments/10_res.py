import pymongo
import pprint
import numpy as np
import datetime
import random
import time
from pymongo import MongoClient

np.random.seed(3)  # set seed so everybody running it gets the same data

client = MongoClient('localhost',27017)  # explicit connect command
db = client.db_boats    

# create UNIQUE INDEX
#db.thePeople.create_index( [('pid', pymongo.ASCENDING)], unique=True )

# the collection we will create
sailors = db.sailors  
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

states = ["AL","AK","AZ","AZ","CA","CO","CT","DE","FL","GA", "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD", "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ", "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC", "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

fNames = ["Bob","Mary","Isabella","Santiago","Valentina","Daniella","Alejandro","Diego","Victoria","Sofia","John","Paul","Peter","Joseph","Vicky","David","Jeffrey","William","Jennifer","Linda","Sarah","Ashley","Michelle","Amy","Julie","Julia","Hannah","Jayden","Noah","Demarco","Madison","Ava","Kayla","Jayla","Priya","Tanya","Neha","Rahul","Raj","Amit","Mohammed","Mohammad","Vivek","Fatimah","Hasan"]

mNames = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

lNames = ["Garcia","Martinez","Gonzalez","Lopez","Torres","Ramirez","Hernandez","Baker","Jackson","Brown","Smith","Jones","Miller","White","Johnson","Wilson","Williams","Anderson","Das","Mukherjee","Simha","Liu","Li","Zhao","Zhang","Wu","Chen","Chan","Lee","Wong","Park","Kim","Ngyuen","Le","Tran","Dang","Sato","Tanaka","Takahashi"]

bNames = ["Carpe Diem", "Beauty", "Marquise", "Siren", "Vida", "Blue Blood", "Leviathan"]
timeStartInsert = datetime.datetime.now()
numDocs = 3
print("\nStart inserting " + str(numDocs) + " documents at: " + str(timeStartInsert) )
for i in range(0,numDocs):
	aFName = fNames[ np.random.randint(len(fNames)) ]
	aMName = mNames[ np.random.randint(len(mNames)) ]
	aLName = lNames[ np.random.randint(len(lNames)) ]
	boatRating = np.random.randint(10)
	aName = aFName + " " + aMName + " " + aLName
	aAge = np.random.randint(100) + 18
	newPerson = {"firstName":aFName, "MI":aMName, "lastName":aLName, "age":aAge, "boatRating": boatRating}
	sailors.insert_one(newPerson)

print("Completed adding sailors")

boats = db.boats

numDocs = 4
for i in range(0, numDocs):
	bName = bNames[np.random.randint(len(bNames))]
	newBoat = {"bname": bName, "rating" : np.random.randint(10)}
	boats.insert_one(newBoat)
print("Added boats")

reservations = db.reservations

allSailors = sailors.find({})
numDocs = np.random.randint(3,10)
for sailor in allSailors:
	for j in range(0,numDocs):
		reservations.insert_one({"sailor": sailor["_id"], "boat" : (boats.aggregate([{ "$sample": { "size": 1 } }]))["_id"], "date": random_date})
		
		

timeEndInsert = datetime.datetime.now()
timeElapsedInsert = timeEndInsert - timeStartInsert
timeStartQueries = datetime.datetime.now()
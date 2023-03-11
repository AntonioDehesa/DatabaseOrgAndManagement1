import pymongo
import pprint
import numpy as np
import datetime
from pymongo import MongoClient

#client = MongoClient()  # connects on default host
client = MongoClient('localhost',27017)  # explicit connect command

db = client.db_people

thePeople = db.thePeople

print("==============Example of updating one record==============")
personToFind = thePeople.find_one({"firstName": "Vivek", "lastName": "Lopez", "state": "MD"})
print(personToFind)
thePeople.update_one({"firstName": "Vivek", "lastName": "Lopez", "state": "MD"}, {"$set": {"salary": 90000}})
personToFind = thePeople.find_one({"firstName": "Vivek", "lastName": "Lopez", "state": "MD"})
print(personToFind)


print("==============Example of updating multiple documents==============")
print("==============First, we show all the people from AK==============")
peopleOfArkansa = thePeople.find({"state":"AK"})
for x in peopleOfArkansa: 
    print(x)
thePeople.update_many({"state":"AK"}, {"$mul": {"salary": 2}})
print("==============Now we print the modified documents==============")
peopleOfArkansa = thePeople.find({"state":"AK"})
for x in peopleOfArkansa: 
    print(x)


print("==============Finally we delete multiple elements==============")
print("==============First we show all the people with a salary over 150000==============")
high_earners = thePeople.find({"salary": {"$gte": 150000}})
for x in high_earners:
    print(x)
print("Now, we delete those records and make sure they were deleted")
thePeople.delete_many({"salary": {"$gte": 150000}})
high_earners = thePeople.find().sort("salary", -1).limit(20)
for x in high_earners:
    print(x)

print("As we can see, the records are no longer there")
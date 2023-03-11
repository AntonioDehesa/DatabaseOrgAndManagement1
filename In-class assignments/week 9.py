import pymongo
import pprint
import numpy as np
import datetime
"""
1) Do the same thing, but create .py file and do it using pymongo

Create a mongodb named “Performances”
Create a collection name Group and insert 5 musician rows. key values should include {name,
numberMembers, costToBook, genre}
Create a collection name Venue and insert 3 venue rows. key values should include {name,
city, seatingCapacity}
Create a collections named UpcomingPerformances with key values: { groupName,
[venueName,date])

2) Continue on and do a find with $regex
3) Continue on and delete one document from a collection using delete_one
4) Continue on and delete two or more documents from a collection using delete_many
"""
from pymongo import MongoClient

#client = MongoClient()  # connects on default host
client = MongoClient('localhost',27017)  # explicit connect command
client.drop_database("Performances")

db = client.Performances    

group = db.Group  
bands = [{"name": "Johns", "numberMembers": 5, "costToBook": 80000, "genre": "Rock"}, 
         {"name": "The cool ones", "numberMembers": 4, "costToBook": 55000, "genre": "Jazz"}, 
         {"name": "Souls", "numberMembers": 6, "costToBook": 45000, "genre": "Country"},
         {"name": "Meh", "numberMembers": 4, "costToBook": 40000, "genre": "something"},
         {"name": "A", "numberMembers": 4, "costToBook": 4, "genre": "yeah"}]
group.insert_many(bands)

venues = db.Venues
places = [{"name": "The palace", "city": "Seatle","seatingCapacity": 50000},
          {"name": "The pearl", "city": "Not Ohio","seatingCapacity": 20000},
          {"name": "Wiiii", "city": "Sidney","seatingCapacity": 80000}]

venues.insert_many(places)

upcomingPerformances = db.UpcomingPerformances
dates = [{"groupName": "Johns", "venueName": "The palace", "date": datetime.datetime(2024,2,2,18,0,0)}]
upcomingPerformances.insert_many(dates)


# Now we find something using regex and directly
found_groups = group.find({"name":"Meh"})
print("Found venues using direct string")
for x in found_groups:
    print(x)

found_venues = venues.find({"name":{"$regex": "ear"}})
print("Found venues using regex")
for x in found_venues:
    print(x)


venues.delete_one({"name": "The palace"})

print("Showing remaining venues after deleeting The palace")
all_venues = venues.find()
for x in all_venues:
    print(x)
    

group.delete_many({'numberMembers': {'$gt': '4'}})

print("Showing remaining groups after deleting groups with 4 members")
all_groups = group.find()
for x in all_groups:
    print(x)
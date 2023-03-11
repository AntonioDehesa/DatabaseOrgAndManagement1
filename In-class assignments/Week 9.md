Create a mongodb named “Performances”
Create a collection name Group and insert 5 musician rows. key values should include {name,
numberMembers, costToBook, genre}
Create a collection name Venue and insert 3 venue rows. key values should include {name,
city, seatingCapacity}
Create a collections named UpcomingPerformances with key values: { groupName,
[venueName,date])


create it:
use Performances

Create a collection and insert 5 musician rows: 

db.Group.insertMany([{name: "Johns", numberMembers: 5, costToBook: 80000, genre: "Rock"}, {name: "The cool ones", numberMembers: 4, costToBook: 55000, genre: "Jazz"}, {name: "Souls", numberMembers: 6, costToBook: 45000, genre: "Country"},{name: "Meh", numberMembers: 4, costToBook: 40000, genre: "something"},{name: "A", numberMembers: 4, costToBook: 4, genre: "yeah"}])

Same for Venue and UpcomingPerformances:

db.Venue.insertMany([{name: "The palace", city: "Seatle",seatingCapacity: 50000},{name: "The pearl", city: "Not Ohio",seatingCapacity: 20000},{name: "Wiiii", city: "Sidney",seatingCapacity: 80000}])

db.UpcomingPerformances.insertMany([{groupName: "Johns", venueName: "The palace", date: new ISODate("2024-02-02T18:00:00Z")}])



now with python

1) Do the same thing, but create .py file and do it using pymongo
2) Continue on and do a find with $regex
3) Continue on and delete one document from a collection using delete_one
4) Continue on and delete two or more documents from a collection using delete_many

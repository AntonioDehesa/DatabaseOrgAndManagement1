
Q1: Complete info about people who have 7 children

# Python
{
    'numChildren': 7
}

# MongoSH
db.thePeople.find({numChildren: 7})

Q2: pid, state, and name of the children for people who have 7 children

# Python

db.thePeople.find_one({"numChildren":7},{"pid":1,"state":1,"children":1})

# MongoSH
db.thePeople.find({numChildren: 7}, {pid:1,state:1,children:1})

Q3: Complete info of people who live in CA and have 6 children

# Python

db.thePeople.find_one({'numChildren': 6, 'state': 'CA'})

# MongoSH
db.thePeople.find({numChildren: 6, state: "CA"})

Q4: Complete info of people who live in CA and have 6 or 7 children

# Python

db.thePeople.find_one({'numChildren': {'$in': [6, 7]}})

# MongoSH
db.thePeople.find({numChildren: {$in:[6,7] }})

Q5: List the pid and children names for all people who have a child whose name contains 'Bob A' => hint - use $regex

# Python

db.thePeople.find_one({'children': {'$regex': 'Bob A' }})

# MongoSH
db.thePeople.find({children: {$regex: 'Bob A' }})

Q6: Aggregation 5: number of poeple who have 0, 1, ... 8 children

# Python

db.thePeople.find_one({'children': {'$regex': 'Bob A' }})

# MongoSH

db.thePeople.aggregate([{"$group": {_id:"$numChildren", numInGroup:{$sum:1}}}, {$sort: {_id: 1}}])

Q7: Aggregation: avgerage salary for each state:

# MongoSH
db.thePeople.aggregate([{$group:{_id:"$state", avgSalary:{$avg:"$salary"}}},{$sort: {_id:1}}])
# Python

db.thePeople.find_one({"$group":{"_id":"$state", "avgSalary":{"$avg":"$salary"}}},{"$sort": {"_id":1}})


Q8: Aggregation: avgerage salary and how many people in the grouping for those living in WI state:

# MongoSH
db.thePeople.aggregate([{$match: {state: "WI"}},{$group:{_id:"$state", avgSalary:{$avg:"$salary"},  numInGroup: {$count: {}}}}])

Q9: Aggregation: average/min/max salary for midwest state:

# MongoSH

db.thePeople.aggregate([{$match: {state: {$in: ["ND", "SD", "NE", "KS", "MN", "IA", "MS", "WI", "IL", "IN", "MI", "OH"]}}},{"$group": {_id:"$state", avgSalary: {$avg: "$salary"}, minSalary: { "$min": "$salary" }, maxSalary: { "$max": "$salary" }, numInGroup:{$sum:1}}}, {$sort: {_id: 1}}])


Q10: Aggregation: avgerage salary in states where the average salary within that state is >= 82,000 and how many people in the grouping for each state: 

# MongoSH

db.thePeople.aggregate([{"$group": {_id:"$state", avgSalary: {$avg: "$salary"}, numInGroup:{$sum:1}}}, {$match: {avgSalary: {$gt : 82000}}}, {$sort: {_id: 1}}])


Q11: Aggregation: average/min/max salary for midwest state whose average salary > 82000:

# MongoSH
db.thePeople.aggregate([{$match: {state: {$in: ["ND", "SD", "NE", "KS", "MN", "IA", "MS", "WI", "IL", "IN", "MI", "OH"]}}},{"$group": {_id:"$state", avgSalary: {$avg: "$salary"}, minSalary: { "$min": "$salary" }, maxSalary: { "$max": "$salary" }, numInGroup:{$sum:1}}}, {$match: {avgSalary: {$gt : 82000}}},{$sort: {_id: 1}}])
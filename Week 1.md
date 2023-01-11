# The ER Model
The Entity-Relationship model is one of the major database design models that are used to figure out how to describe data. 
The database design process has three different parts to it. There's conceptual database design, logical database design, and physical. 
## Conceptual database design
It is thinking about the data and being able to understand it from a conceptual level. 
We think about the data itself, the objects, semantic objects, relationships it has, all to get an abstract, but complete description of the data. 

## Logical database design
It is the logical mathematical model.
In here, we transform the conceptual design into a formal schema expressed in the chosen data model, to get a precise and complete model. 

## Physical database design 
It is how you set up the performance of the database, laying it out on disk, and creating indexes.
The goal is to get good performance. 

When you design your database, you start with the information up at the top. Then you go through a conceptual database design where you map it into a conceptual data model. In this case, the ER model. 

Then you map it to a logical model. Finally, to a physical model, which will be discusses at a later time.


For this particular model, an entity is an object, for example, a car, and a person. 
And they can relationships. For example, a person can own a car. 

We have also the example of a library, the authors, the books. 

## Cardinality Constraints 

They relate entity set one to entity set two. They can be: 
* N to M
* N to 1
* 1 to N
* 1 to 1

If no constraint is specified, it defaults to N or M. 
You can also specify: 0 to N, or 1 to N, or 0 to 1, etc. 

### Crow´s foot Notation
A more condensed, more graphically "pleasant" way to show the same ER model. 

# Class
When creating a Entity Relational Diagram, we have some elements. 

## Entities

We can identify them as Nouns: Chairs, buildings, children, etc. 

### Descriptions
The entities need descriptions, such as names, age, etc. 
## Relationships

These are mostly verbs: teaches, votes, does, etc. 
Relationships require cardinality constraints. 
# Relational Algebra
q2

What is the name of all food items that have fewer than 600 calories and cost less than 2.50?

project name | select price < 2.50 | select calories < 600 | FoodItem

q3

What is the order ID for orders made on 2019-02-14 that included two or more items called “tuna roll”?

x = project orderID | select oDate = 2019-02-14 | Order
y = project itemID | select quantity >= 2 | (x equi join PartOfOrder)
z = select name | (y equi join FoodItem)

project Order.orderID | select PartOfOrder.quantity >= 2 | select FoodItem.name = "tuna roll" | select Order.oDate = 2019-02-14 | (FoodItem equi join PartOfOrder equi join Order)

q4

Find the name of customers who have ordered one or more of each and every food item.

Let R = project itemID | FoodItem
Let S = project Customer.name, PlacedOrder.orderID | (Customer equi join PlacedOrder)
Let T = project S.name, PartOfOrder.itemID | (S equi join PartOfOrder)
Let U = T / R
where / = Division


# SQL
q5

Find the name and custID of all customers born on 1999-12-31.

select c.name, c.custID from Customer c where c.bdate = "1999-12-31"

q6

Find the name of customers who have ordered (any quantity >= 1) the food item “smellyFish” on 2019-01-01.

select c.name from customer c, placedorder pO, partoforder poo, Orderg o, fooditem fi
where c.custID = po.custID 
and
po.orderID = poo.orderID
and
o.orderID = po.orderID
and
poo.itemID = fi.itemID
and
o.oDate = "2019-01-01"
and
fi.name = "smellyFish"


q7

A new manager has decided all food items will cost $1, $2, $5, $10, or $20. Find the average number of calories for all food items that cost the same amount for each of the different dollar amounts. Your query should be flexible to adding new/different dollar amounts; hence, it should work for any number of price groups.
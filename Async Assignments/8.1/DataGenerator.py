import numpy as np

np.random.seed(1) 

colors = []
colors.append('red') 
colors.append('green') 
colors.append('blue') 
colors.append('yellow') 
colors.append('orange')
colors.append('purple')
colors.append('grey') 
colors.append('brown') 
colors.append('gold') 
colors.append('silver') 
colors.append('pink') 
colors.append('moss') 
colors.append('perwinkle') 
colors.append('pumpkin') 
colors.append('black') 
colors.append('citron') 
colors.append('coffee')
colors.append('chocolate') 
colors.append('olive') 
colors.append('peach')
colors.append('burnt umber') 
colors.append('salmon') 
colors.append('teal') 
colors.append('vermilion') 
colors.append('white') 
colors.append('ivory') 
colors.append('grape') 
colors.append('lemon')
colors.append('lime') 

# create the sailors data
numSailors = 8 
outfile = open("data_sailors","w") 
for i in range(1,numSailors+1):
	outString = ''
	outString += str(i)   # id
	outString += ','
	outString += 'Bob'
	outString += str(i)   # name
	outString += ','
	age = str( np.random.randint(80) + 18)   
	outString += age  # age
	outString += ','
	rating = ( np.random.randint(10) + 1 )
	outString += str(rating)   # rating
	outString += "\n"
	outfile.write(outString)
outfile.close()

# create the boats data
numBoats = 8 
outfile = open("data_boats","w") 
for i in range(101,numBoats+101):
	outString = ''
	outString += str(i)   # bid
	outString += ','
	outString += 'guppy'
	outString += str(i)   #bname
	outString += ','
	ratingNeeded = str( np.random.randint(10) + 1)  # rating need to rserve
	outString += ratingNeeded
	outString += ','
	rNum = np.random.randint(29)
	outString += colors[rNum]   # bcolor
	outString += "\n"
	outfile.write(outString)
outfile.close()



# create the reserve data
numReservations = 40 
outfile = open("data_reserve","w") 
for i in range(1,numReservations+1):
	outString = ''
	bid = str( np.random.randint(numBoats) + 101)  
	outString += str(bid)   # bid
	outString += ','
	sid = str( np.random.randint(numSailors) + 1)  
	outString += sid   # sid
	outString += ','
	date = '2013-'
	date += str( np.random.randint(12) + 1)  
	date += '-'
	date += str( np.random.randint(28) + 1)  
	outString += date
	outString += "\n"
	outfile.write(outString)
outfile.close()


# Entities
Passholder ( passId, name, age, streetAddress, city, state )
Resort ( resortName, city, state, baseElevation, verticalFeet )
Lift ( liftNumber, baseElevation, topElevation, numberSeats, speed, resortName, city, state )
# Relationship
validAt ( passID, resortName )

Rode ( passID, liftNumber, date, time )
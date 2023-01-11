# Entities
Passholder ( passId, name, age, streetAddress, city, state )
Resort ( resortName, city, state, baseElevation, verticalFeet )
Lift ( liftNumber, baseElevation, topElevation, numberSeats, speed )
# Relationship
validAt ( passID, resortName ) // In this case, I chose resortName and passID, as city and state are already defined in the passholder

partOf ( resortName, city, state, liftNumber ) // In this case, I chose resortName, city, and state as necessary, as there can be multiple resorts with the same name (unlikely, but still possible), and there can be two or more cities with the same name, but by including the state, we guarantee no repeated entries.  

Rode ( passID, liftNumber, date, time )
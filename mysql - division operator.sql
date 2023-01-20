select distinct passID, name
from passHolder as ph
where not exists 
(select liftNumber 
	from rode 
    where liftNumber not in 
		(select liftNumber
			from rode as r 
            where ph.passID = r.passID
		)
);
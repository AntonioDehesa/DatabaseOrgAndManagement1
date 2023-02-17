Create a stored procedure to insert three new employees (calling the procedure three times): 
employee ids of 20, 21, 22 and having them work for departments 101, 103, 
and 105 respectively.


Delimiter \\
Create procedure proc_addEmployeeAndRole(IN inSID INT, IN inName VARCHAR(20), IN inAge INT, IN inSalary INT, in inResidenceState char(2), in inStartDate date, in indid int)
begin
  insert into employee values (inSID, inName, inAge, inSalary, inResidenceState, inStartDate);
  insert into worksfor values (inSID, indid, inStartDate); 
end\\
delimiter ;


call proc_addEmployeeAndRole(20, "John", 35, 55000, "OH", "1999-02-02", 101);
call proc_addEmployeeAndRole(21, "Mike", 40, 65000, "TX", "2000-08-07", 103);
call proc_addEmployeeAndRole(22, "Something", 55, 75000, "OK", "2005-06-12", 105);
#IN inSID INT, IN inName VARCHAR(20), IN inAge INT, IN inSalary INT, in inResidenceState char(2), in inStartDate date, in indid int



Now using if then else end if:  crate code so that it will give you an error message if you attempt to load an employee whose EID already exists, otherwise loads it
Delimiter \\
Create procedure proc_addEmployeeAndRoleAvoidDuplicate(IN inSID INT, IN inName VARCHAR(20), IN inAge INT, IN inSalary INT, in inResidenceState char(2), in inStartDate date, in indid int)
begin
IF inSID in (select eid from employee)
then
	SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Duplicate key: The employee ID already exists';
ELSE
   insert into employee values (inSID, inName, inAge, inSalary, inResidenceState, inStartDate);
   insert into worksfor values (inSID, indid, inStartDate); 
END IF;

end\\
delimiter ;



call proc_addEmployeeAndRoleAvoidDuplicate(20, "John", 35, 55000, "OH", "1999-02-02", 101);
call proc_addEmployeeAndRoleAvoidDuplicate(21, "Mike", 40, 65000, "TX", "2000-08-07", 103);
call proc_addEmployeeAndRoleAvoidDuplicate(22, "Something", 55, 75000, "OK", "2005-06-12", 105);
#IN inSID INT, IN inName VARCHAR(20), IN inAge INT, IN inSalary INT, in inResidenceState char(2), in inStartDate date, in indid int


CREATE TABLE sailorIndexed SELECT * FROM sailors;
ALTER TABLE sailorIndexed ADD INDEX (rating);
Q. Find the number of sailors who had a reservation in which their rating was exactly equal to the rating needed of the reserved boat.

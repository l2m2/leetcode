CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select salary from (
	    select A.*, @rowid := @rowid + 1 AS row_num
	    from 
	    (
		    select salary
		    from Employee
		    group by salary 
		    order by salary desc 
	    ) A, (SELECT @rowid := 0) dummy
    ) B
    where row_num = N
  );
END
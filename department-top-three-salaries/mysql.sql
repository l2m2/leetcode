select t4.name as Department, t3.name as Employee, t2.salary as Salary from (
	select departmentId, salary from (
		select departmentId, salary,
		row_number() over( partition by departmentId order by salary desc ) as row_num
		from Employee
		group by departmentId, salary
	) t1 where row_num <= 3
) t2 left join Employee t3 on t2.departmentId = t3.departmentId and t2.salary = t3.salary
left join Department t4 on t2.departmentId = t4.id
order by Department, Salary desc
select t3.name as Department, t2.name as Employee, t1.salary as Salary  from (
  select departmentId, max(salary) as salary
  from Employee
  group by departmentId
) t1 
left join Employee t2 on t1.departmentId = t2.departmentId and t1.salary = t2.salary
left join Department t3 on t1.departmentId = t3.id

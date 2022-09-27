-- Solution 1
select t1.name as Employee 
from (select * from Employee where managerId is not null) t1
left join Employee t2 on t1.managerId = t2.id
where t1.salary > t2.salary


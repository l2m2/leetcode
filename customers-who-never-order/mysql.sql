-- Solution 1
select name as Customers 
from Customers c
where not exists ( select * from Orders where customerId = c.id )

-- Solution 2
select name as Customers
from Customers c
left join Orders o on c.id = o.customerId
where o.id is null
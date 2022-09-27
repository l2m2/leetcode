delete from Person where id not in (
 select min(id) as min_id
 from Person
 group by email
)
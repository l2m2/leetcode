with t1 as (
    select * from Trips where request_at >= '2013-10-01' and request_at <= '2013-10-03'
), t2 as (
    select t1.* from t1 
    left join Users u1 on t1.client_id = u1.users_id
    left join Users u2 on t1.driver_id = u2.users_id
    where u1.banned = 'No' and u2.banned = 'No'
)
select request_at as `Day`, 
round(count(case when status != 'completed' then 1 else null end) / count(*), 2) as `Cancellation Rate`
from t2 
group by request_at
order by 1
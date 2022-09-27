-- Solution 1
select id
from Weather t1
where temperature > (select temperature from Weather where recordDate = subdate(t1.recordDate, 1))

-- Solution 2
select t1.id from (
 select id, temperature, subdate(recordDate, 1) as yesterday from Weather
) t1 left join Weather t2 on t1.yesterday = t2.recordDate
where t1.temperature > t2.temperature
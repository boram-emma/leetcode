# Write your MySQL query statement below
select w.id as Id
from Weather w
join Weather t on w.recordDate = DATE_ADD(t.recordDate, INTERVAL 1 DAY)
where w.temperature > t.temperature 

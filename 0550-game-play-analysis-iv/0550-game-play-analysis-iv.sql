# Write your MySQL query statement below
WITH firstday as (
    select player_id, MIN(event_date) as event_date
    from Activity
    group by player_id
)


SELECT 
    ROUND(count(DISTINCT a.player_id)/(SELECT count(DISTINCT player_id) FROM Activity),2) 
    AS fraction
FROM Activity a
JOIN firstday f ON a.player_id = f.player_id 
AND a.event_date = DATE_ADD(f.event_date, INTERVAL 1 DAY)
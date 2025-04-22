# Write your MySQL query statement below

# remove all rows which have same (lat, lon)
# GROUP BY

SELECT SUM(f.tiv_2016) AS tiv_2016
FROM (
    SELECT ROUND(SUM(r.tiv_2016),2) AS tiv_2016
    FROM (
        SELECT *
        FROM Insurance i
        GROUP BY i.lat, i.lon
        HAVING COUNT(*) <= 1 
    ) AS r
    GROUP BY r.tiv_2015
    HAVING COUNT(*) >= 2
) AS f
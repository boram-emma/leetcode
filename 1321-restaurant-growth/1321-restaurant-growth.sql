# Write your MySQL query statement below
# moving average > partition by

WITH daily_amount AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)

SELECT 
    c.visited_on, 
    SUM(u.amount) AS amount, 
    ROUND(AVG(u.amount),2) AS average_amount
FROM daily_amount c
JOIN daily_amount u on u.visited_on 
    BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
GROUP BY c.visited_on
HAVING COUNT(DISTINCT u.visited_on) = 7
ORDER BY c.visited_on

-- SELECT 
--     a.visited_on,
--     SUM(b.amount) AS amount,
--     ROUND(AVG(b.amount), 2) AS average_amount
-- FROM Customer a
-- JOIN Customer b 
--   ON b.visited_on BETWEEN DATE_SUB(a.visited_on, INTERVAL 6 DAY) AND a.visited_on
-- GROUP BY a.visited_on
-- HAVING COUNT(DISTINCT b.visited_on) = 7
-- ORDER BY a.visited_on;
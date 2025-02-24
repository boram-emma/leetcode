# Write your MySQL query statement below
-- WITH boarding AS (
--     SELECT person_name, turn, 
--            SUM(weight) OVER (ORDER BY turn) AS total_weight
--     FROM Queue
-- )
-- SELECT person_name
-- FROM boarding
-- WHERE total_weight <= 1000
-- ORDER BY total_weight DESC
-- LIMIT 1;


WITH cumulQue AS (
    SELECT *,
            SUM(weight) OVER (ORDER BY turn) AS cumul
    FROM Queue
)

SELECT c.person_name AS person_name
FROM cumulQue c
WHERE c.cumul <= 1000
ORDER BY c.cumul DESC
LIMIT 1;
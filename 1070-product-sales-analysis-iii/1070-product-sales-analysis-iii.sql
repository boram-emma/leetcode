# Write your MySQL query statement below
WITH firstYear AS (
    SELECT s.product_id, MIN(s.year) AS first_year
    FROM Sales s
    LEFT JOIN Product p ON s.product_id = p.product_id
    GROUP BY s.product_id
)

SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN firstYear f ON s.product_id = f.product_id AND s.year = f.first_year
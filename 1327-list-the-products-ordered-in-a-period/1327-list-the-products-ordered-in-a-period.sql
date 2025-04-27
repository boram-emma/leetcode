# Write your MySQL query statement below
SELECT p.product_name, sum(o.unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND DATE_ADD('2020-02-01', INTERVAL 28 DAY)
GROUP BY p.product_name
HAVING sum(o.unit) >= 100
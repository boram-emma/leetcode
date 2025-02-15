# Write your MySQL query statement below
SELECT p.product_id, 
       IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u 
ON p.product_id = u.product_id 
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;



-- select p.product_id, 
--         ifnull(round(sum(u.units*p.price)/sum(u.units),2),0) as average_price 
-- from UnitsSold u
-- right join Prices p on p.product_id = u.product_id
-- AND u.purchase_date BETWEEN p.start_date AND p.end_date
-- group by p.product_id
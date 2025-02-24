
WITH latest_date AS (
    SELECT p.product_id, p.new_price, p.change_date, 
            ROW_NUMBER() OVER (PARTITION BY p.product_id ORDER BY p.change_date DESC) AS rnk
    FROM Products p
    WHERE p.change_date <= '2019-08-16'
)

SELECT p.product_id, COALESCE(ld.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN latest_date ld 
ON p.product_id = ld.product_id AND ld.rnk = 1


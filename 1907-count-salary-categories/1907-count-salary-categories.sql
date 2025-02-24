# Write your MySQL query statement below
WITH cate_accounts AS (
    SELECT *, CASE 
                WHEN income < 20000 THEN "Low Salary"
                WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
                WHEN income >= 50000 THEN "High Salary"
               END AS cate
    FROM Accounts
),
categories AS (
    SELECT "Low Salary" AS category
    UNION ALL
    SELECT "Average Salary"
    UNION ALL
    SELECT "High Salary"
)


SELECT c.category AS category, COUNT(ca.cate) AS accounts_count
FROM categories c
LEFT JOIN cate_accounts ca ON c.category = ca.cate
GROUP BY c.category
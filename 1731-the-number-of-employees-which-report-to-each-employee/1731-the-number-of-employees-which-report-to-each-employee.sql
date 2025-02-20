# Write your MySQL query statement below

SELECT e.employee_id, e.name, COUNT(ee.reports_to) AS reports_count, ROUND(AVG(ee.age),0) AS average_age
FROM Employees e
JOIN Employees ee ON e.employee_id = ee.reports_to
GROUP BY e.employee_id
ORDER BY employee_id
# Write your MySQL query statement below
select coalesce(u.unique_id, NULL) as unique_id, e.name 
from EmployeeUNI u
right join Employees e on u.id = e.id; 
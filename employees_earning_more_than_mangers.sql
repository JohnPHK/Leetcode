# Write your MySQL query statement below
select a.name as 'Employee'
from Employee as a, Employee as b
where a.managerId = b.Id and a.Salary > b.Salary ;
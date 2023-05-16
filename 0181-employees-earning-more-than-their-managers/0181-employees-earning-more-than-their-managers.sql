# Write your MySQL query statement below
SELECT tmp.name AS Employee FROM (
SELECT e2.*, e1.salary AS managerSalary FROM Employee e1 RIGHT JOIN Employee e2 ON e1.id=e2.managerId) AS tmp
WHERE tmp.salary > tmp.managerSalary;
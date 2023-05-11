CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT 
        CASE 
            WHEN (SELECT COUNT(DISTINCT(salary)) FROM Employee) < N THEN NULL
            ELSE (SELECT DISTINCT(salary) FROM Employee ORDER BY salary DESC LIMIT M, 1) 
        END AS NthHighestSalary
  );
END
# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
SELECT
	id,
	LAG(num) OVER (
	ORDER BY id) AS PrevNum,
	num,
	LEAD(num) OVER (
	ORDER BY id) AS NextNum FROM Logs ) AS tmp
WHERE num = PrevNum AND num = NextNum;

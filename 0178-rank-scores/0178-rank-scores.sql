# Write your MySQL query statement below
SELECT s3.score, CASE WHEN tmp.ranking=0 THEN 1 ELSE tmp.ranking END AS `rank` 
FROM scores s3 
JOIN 
    (SELECT s1.id, s1.score, (SELECT COUNT(DISTINCT(s2.score)) FROM scores s2 WHERE s2.score        >= s1.score) AS ranking FROM scores s1) AS tmp ON tmp.id=s3.id 
ORDER BY s3.score DESC;

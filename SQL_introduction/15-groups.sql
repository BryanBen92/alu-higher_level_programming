-- Count records at each score, largest group first.
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;

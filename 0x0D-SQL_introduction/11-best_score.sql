-- lists all records with score >= 10 in a descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

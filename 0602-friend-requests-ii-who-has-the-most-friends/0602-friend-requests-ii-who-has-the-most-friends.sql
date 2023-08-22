WITH Temp AS
(SELECT requester_id AS id FROM RequestAccepted
UNION ALL SELECT accepter_id FROM RequestAccepted)

SELECT id, count(*) AS num FROM Temp
GROUP BY id ORDER BY num DESC LIMIT 1
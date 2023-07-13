SELECT W1.id FROM Weather W1 INNER JOIN Weather W2
ON ADDDATE(W1.recordDate, -1) = W2.recordDate
WHERE W1.temperature > W2.temperature;
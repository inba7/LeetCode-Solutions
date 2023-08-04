SELECT s.user_id, ROUND(SUM(CASE when action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(1) , 2) AS confirmation_rate FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id GROUP BY user_id;
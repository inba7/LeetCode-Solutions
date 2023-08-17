SELECT person_name FROM 
( SELECT person_name, turn,
  SUM(weight) OVER (ORDER BY turn) AS Total
  FROM Queue
) A WHERE Total <= 1000 ORDER BY turn DESC LIMIT 1
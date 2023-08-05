with cte as
    (SELECT player_id, event_date, DATE_SUB(event_date, INTERVAL 1 DAY) = 
    MIN(event_date) OVER (partition by player_id) AS r FROM activity)
SELECT ROUND(SUM(r)/COUNT(distinct player_id), 2) AS fraction FROM cte
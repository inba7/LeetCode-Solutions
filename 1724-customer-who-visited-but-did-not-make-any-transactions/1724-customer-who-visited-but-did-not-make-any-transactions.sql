SELECT customer_id, count(Visits.visit_id) AS count_no_trans 
FROM Visits WHERE visit_id not IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
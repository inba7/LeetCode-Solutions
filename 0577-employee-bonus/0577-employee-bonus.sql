SELECT E.name, B.bonus FROM Employee E LEFT JOIN Bonus B
ON E.empId = B.empId WHERE (bonus < 1000 or bonus is null);
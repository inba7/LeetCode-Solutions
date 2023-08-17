WITH Temp AS(
SELECT D.Name AS Department, 
E.Name AS Employee, 
E.Salary AS Salary,
dense_rank() OVER (partition by D.Name ORDER BY E.Salary DESC) AS Ranking
FROM Employee E 
LEFT JOIN Department D ON E.DepartmentId = D.Id) 

SELECT Department, Employee, Salary
FROM Temp WHERE Ranking <=3
SELECT M.name FROM Employee E INNER JOIN Employee M
ON E.managerId = M.id GROUP BY E.managerId HAVING COUNT(E.id) >= 5;
SELECT M.name FROM Employee E INNER JOIN Employee M
ON E.managerId = M.id WHERE E.managerId IS NOT NULL
GROUP BY E.managerId HAVING COUNT(E.managerId) >= 5
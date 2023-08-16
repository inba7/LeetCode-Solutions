WITH Temp AS
(SELECT num, lead(num,1) over() num1,
lead(num,2) over() num2 FROM logs)

SELECT DISTINCT num ConsecutiveNums FROM Temp 
WHERE (num=num1) AND (num=num2)
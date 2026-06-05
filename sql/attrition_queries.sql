SELECT Department,
COUNT(*) AS Employees
FROM employees
GROUP BY Department;

SELECT Department,
AVG(Salary) AS AvgSalary
FROM employees
GROUP BY Department;

SELECT Attrition,
COUNT(*) AS Total
FROM employees
GROUP BY Attrition;

SELECT Promotion,
COUNT(*) AS Total
FROM employees
GROUP BY Promotion;
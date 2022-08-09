SELECT
   Department,
   Employee,
   Salary
FROM(SELECT
        dense_rank() OVER (partition BY DepartmentId ORDER BY Salary DESC) AS rang,
        Employee.Name AS Employee,
        Salary,
        Department.Name AS Department
     FROM Department INNER JOIN Employee
     ON Employee.DepartmentId=Department.Id)as top
WHERE rang<=3
ORDER BY Department, rang
;
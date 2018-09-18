/*
 * @File: ms.sql
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2018-09-17 22:52:36
 * @Last Modified By: leon.li(l2m2lq@gmail.com>)
 * @Last Modified Time: 2018-09-17 23:10:02
 */
-- 解法1
SELECT TOP 1 Salary AS SecondHighestSalary FROM (
  SELECT Salary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)
  UNION ALL
  SELECT NULL
) A ORDER BY Salary DESC

-- 解法2
SELECT Top 1 Salary AS SecondHighestSalary FROM (
		SELECT Salary, ROW_NUMBER() OVER (ORDER BY Salary DESC) AS Num
		FROM Employee
		GROUP BY Salary 	
		UNION
		SELECT NULL, 2
) A 
WHERE A.Num = 2
ORDER BY Salary DESC

-- 解法3
SELECT TOP 1 lag("Salary") OVER (ORDER BY "Salary" ) AS "SecondHighestSalary"
FROM (
SELECT "Salary" FROM "Employee" GROUP BY "Salary"
) A
ORDER BY "Salary" DESC

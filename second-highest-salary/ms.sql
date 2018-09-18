/*
 * @File: ms.sql
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2018-09-17 22:52:36
 * @Last Modified By: leon.li(l2m2lq@gmail.com>)
 * @Last Modified Time: 2018-09-17 23:10:02
 */
SELECT TOP 1 Salary AS SecondHighestSalary FROM (
  SELECT Salary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)
  UNION ALL
  SELECT NULL
) A ORDER BY Salary DESC
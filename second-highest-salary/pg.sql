/*
 * @File: pg.sql
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2018-09-18 11:06:32
 * @Last Modified By: leon.li(l2m2lq@gmail.com>)
 * @Last Modified Time: 2018-09-18 11:42:54
 */

SELECT lag("Salary") OVER (ORDER BY "Salary" ) AS "SecondHighestSalary"
FROM (
SELECT "Salary" FROM "Employee" GROUP BY "Salary"
) A
ORDER BY "Salary" DESC
LIMIT 1
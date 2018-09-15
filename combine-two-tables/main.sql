/*
 * @File: main.sql
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2018-09-15 22:51:19
 * @Last Modified By: leon.li(l2m2lq@gmail.com>)
 * @Last Modified Time: 2018-09-15 22:51:38
 */

SELECT FirstName, Lastname, City, State
FROM Person AS P 
LEFT JOIN Address AS A
ON P.PersonId = A.PersonId
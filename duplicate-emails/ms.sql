/*
 * @File: ms.sql
 * @Author: leon.li(l2m2lq@gmail.com)
 * @Date: 2018-09-19 23:53:13
 * @Last Modified By: leon.li(l2m2lq@gmail.com>)
 * @Last Modified Time: 2018-09-20 00:03:25
 */

-- 解法1
SELECT Email 
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1 

-- 解法2
-- 用窗口函数
-- TODO
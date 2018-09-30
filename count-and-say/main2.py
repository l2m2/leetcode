'''
@File: main2.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-10-01 00:08:47
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-10-01 00:20:12
'''

class Solution:
  def _count(self, s):
    last_num = '0'
    tmp = ''
    for i in s:
      if i != last_num:
        if last_num != '0':
          tmp += (str(count)+last_num)
        last_num = i
        count = 1
      else:
        count += 1
    return tmp + (str(count) + last_num)
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1: return "1"
    elif n == 2: return "11"
    s = "11"
    for _ in range(3, n+1):
      s = self._count(s)
    return s

if __name__ == "__main__":
  s = Solution()
  print(s.countAndSay(1) == "1")
  print(s.countAndSay(3) == "21")
  print(s.countAndSay(4) == "1211")
  print(s.countAndSay(5) == "111221")
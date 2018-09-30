'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-30 23:22:53
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-10-01 00:03:24
'''

class Solution:
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1: 
      return "1"
    elif n == 2:
      return "11"
    s = "11"
    m = 3
    while m <= n:
      count = 0
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
      tmp += (str(count) + last_num)
      s = tmp
      m += 1
    return s

if __name__ == "__main__":
  s = Solution()
  print(s.countAndSay(1) == "1")
  print(s.countAndSay(3) == "21")
  print(s.countAndSay(4) == "1211")
  print(s.countAndSay(5) == "111221")
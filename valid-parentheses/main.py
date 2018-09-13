'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-13 17:05:18
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-13 17:43:55
'''

class Solution:
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    buff = []
    dict_buff = { '(': ')', '[': ']', '{': '}' }
    for i in s:
      if i in dict_buff:
        buff.append(i)
      else:
        if buff and i == dict_buff[buff[-1]]:
          buff.pop()
        else:
          return False
    return len(buff) == 0 

if __name__ == "__main__":
  so = Solution()
  print(so.isValid("()"))
  print(so.isValid("()[]{}"))
  print(so.isValid("(]"))
  print(so.isValid("([)]"))
  print(so.isValid("{[]}"))
  print(so.isValid(""))
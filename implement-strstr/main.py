'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-14 18:20:21
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-15 00:19:38
'''

class Solution:
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
      return 0
    l = len(needle)
    for i in range(len(haystack)):
      if haystack[i:l+i] == needle:
        return i
    return -1

if __name__ == "__main__":
  so = Solution()
  print(so.strStr("hello", "ll") == 2)
  print(so.strStr("hello", "ew") == -1)
  print(so.strStr("h", "h") == 0)
  print(so.strStr("", "") == 0)
  print(so.strStr("", "rr") == -1)
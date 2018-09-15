'''
@File: main2.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-15 00:22:34
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-15 21:43:25
'''

class Solution:
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    len_needle = len(needle)
    len_haystack = len(haystack)
    if len_needle == 0:
      return 0
    j = 0
    for i in range(len_haystack):
      while haystack[i] == needle[j]:
        i += 1
        j += 1
        if j == len_needle:
          return i - len_needle
        if i == len_haystack:
          return -1
      j = 0 
    return -1 

if __name__ == "__main__":
  so = Solution()
  print(so.strStr("hello", "ll") == 2)
  print(so.strStr("hello", "ew") == -1)
  print(so.strStr("h", "h") == 0)
  print(so.strStr("", "") == 0)
  print(so.strStr("", "rr") == -1)
  print(so.strStr("aaaa", "aaa") == 0)
  print(so.strStr("aaa", "aaaa") == -1)
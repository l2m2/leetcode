'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-13 15:42:39
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-13 16:25:11
'''


class Solution:
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
      return ""
    first = strs[0]
    if len(strs) == 1:
      return first
    index = -1
    for i in range(len(first)):
      for c in strs[1:]:
        if i >= len(c) or first[i] != c[i]:
          return first[:index+1]
      index = i 
    return first[:index+1]
        
if __name__ == "__main__":
  so = Solution()
  print(so.longestCommonPrefix(["flower","flow","flight"]) == "fl")
  print(so.longestCommonPrefix(["dog","racecar","car"]) == "")
  print(so.longestCommonPrefix(["aa","a"]) == "a")
  print(so.longestCommonPrefix(["a"]) == "a")
  print(so.longestCommonPrefix(["c","c"]) == "c")
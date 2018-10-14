class Solution:
  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = s.rstrip()
    n = len(s) - 1
    m = 0
    while n >= 0:
      if s[n] != ' ':
        m += 1
      else:
        break
      n -= 1
    return m

if __name__ == "__main__":
  s = Solution()
  print(s.lengthOfLastWord('Hello World') == 5)
  print(s.lengthOfLastWord('') == 0)
  print(s.lengthOfLastWord('a ') == 1)
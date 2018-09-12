
class Solution:
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    xx = x if x > 0 else -x
    arr = []
    while xx:
      arr.append(xx % 10)
      xx = xx // 10
    xx = 0
    factor = 1
    for i in arr[::-1]:
      xx += i * factor
      factor *= 10
      if xx > 2**31 - 1 or xx < -2**31:
        return 0
    return xx if x > 0 else -xx

if __name__ == "__main__":
  so = Solution()
  print(so.reverse(120) == 21)
  print(so.reverse(-123) == -321)
  print(so.reverse(123) == 321)
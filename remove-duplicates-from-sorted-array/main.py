'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-13 19:27:14
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-15 00:00:02
'''

class Solution:
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    le = len(nums)
    if le == 0: return 0
    if le == 1: return 1
    start, end = 0, 1
    while start < (le - 1) and nums[start] <= nums[end]:
      if nums[end] == nums[start]:
        if end == le - 1:
          break
        temp = nums[end]
        for i in range(end, le - 1):
          nums[i] = nums[i+1]
        nums[-1] = temp
      else:
        start += 1
        end += 1
    return start + 1

if __name__ == "__main__":
  so = Solution()
  nums = [1, 2, 2, 3, 3, 4, 4]
  # nums = [1, 1]
  # nums is passed in by reference. (i.e., without making a copy)
  le = so.removeDuplicates(nums)
  # any modification to nums in your function would be known by the caller.
  # using the length returned by your function, it prints the first len elements.
  print(nums[:le])

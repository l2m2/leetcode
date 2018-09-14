
'''
@File: main2.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-14 10:11:16
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-14 17:30:33
'''

class Solution:
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    start = 0
    for i in range(1, len(nums)):
      if nums[i] != nums[i-1]:
        start += 1
        nums[start] = nums[i]
    return start + 1

if __name__ == "__main__":
  so = Solution()
  # nums = [1, 2, 2, 3, 3, 4, 4]
  nums = [1]
  # nums = [1, 2, 2, 2]
  # nums = [0,0,1,1,1,2,2,3,3,4]
  # nums is passed in by reference. (i.e., without making a copy)
  # nums = [i for i in range(-999, 999)]
  le = so.removeDuplicates(nums)
  # any modification to nums in your function would be known by the caller.
  # using the length returned by your function, it prints the first len elements.
  print(nums[:le])
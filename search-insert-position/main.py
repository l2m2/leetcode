'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-15 21:54:00
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-15 22:05:29
'''

class Solution:
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
      if nums[i] == target:
        return i
      elif nums[i] > target:
        return i
    return len(nums)

if __name__ == "__main__":
  so = Solution()
  nums = [1,3,5,6]
  print(so.searchInsert(nums, 5) == 2)
  print(so.searchInsert(nums, 2) == 1)
  print(so.searchInsert(nums, 7) == 4)
  print(so.searchInsert(nums, 0) == 0)
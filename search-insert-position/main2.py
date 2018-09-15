'''
@File: main2.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-15 22:08:03
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-15 22:39:33
'''

class Solution:
  def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    if left == right and nums[left] < target:
      return left + 1
    return left

if __name__ == "__main__":
  so = Solution()
  nums = [1,3,5,6]
  print(so.searchInsert(nums, 5) == 2)
  print(so.searchInsert(nums, 2) == 1)
  print(so.searchInsert(nums, 7) == 4)
  print(so.searchInsert(nums, 0) == 0)
  print(so.searchInsert([2,3,5,6], 2) == 0)
  print(so.searchInsert([2,3,5,6], 4) == 2)
  print(so.searchInsert([1,3,5,7], 6) == 3)
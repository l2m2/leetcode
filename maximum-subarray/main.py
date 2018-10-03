'''
@File: main.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-10-02 14:17:25
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-10-03 20:26:29
'''

class Solution:
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    # 用最小的负数二分
    min_num = min(nums)
    # 若最小值为自然数，全部相加
    if min_num >= 0:
      return sum(nums)
    max_num = max(nums)
    # 若最大值为负数，返回最大值
    if max_num < 0:
      return max_num
    # 用负数二分
    sums = []
    sums.append(sum(nums))
    for i in range(len(nums)):
      if nums[i] < 0:
        if i > 0:
          sums.append(self.maxSubArray(nums[:i]))
        if i < len(nums) - 1:
          sums.append(self.maxSubArray(nums[i+1:]))
    return max(sums)

if __name__ == "__main__":
  s = Solution()
  print(s.maxSubArray([3,-4,8,-5,15]) == 18)
  print(s.maxSubArray([3,-4,5,3,-5,6,9]) == 18)
  print(s.maxSubArray([31,-41,59,26,-53,58,97]) == 187)
  print(s.maxSubArray([31,-41,59,26,-53,58,97,-93,-23,84]) == 187)
  print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
  print(s.maxSubArray([-2,4,-3,-3,2,2,1,1,-5]) == 6)
  print(s.maxSubArray([-1,-1,-1,-1]) == -1)
  print(s.maxSubArray([-1]) == -1)
  print(s.maxSubArray([]) == 0)
  print(s.maxSubArray([-1,-2,-3,-4]) == -1)
  print(s.maxSubArray([1,2,3,4]) == 10)
  print(s.maxSubArray([-2,-5,3,-4,-5,1,-3]) == 3)


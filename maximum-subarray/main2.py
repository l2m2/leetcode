'''
@File: main2.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-10-09 23:08:09
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-10-09 23:30:15
'''

'''
联机算法实现
'''
class Solution:
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 检查是否为空
    if not nums:
      return 0
    # 检查是否为全负数
    if max(nums) < 0:
      return max(nums)
    # 序列中肯定包含正数
    # 则证明：最大子序列的和肯定为正数
    # 则：相加小于0的不处理
    max_sum = 0
    cur_sum = 0
    for num in nums:
      cur_sum += num
      if cur_sum > max_sum:
        max_sum = cur_sum
      if cur_sum < 0:
        cur_sum = 0
    return max_sum
    
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


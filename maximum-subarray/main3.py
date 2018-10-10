'''
@File: main3.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-10-10 23:19:01
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-10-11 00:02:27
'''

'''
分治算法实现
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
    left, right = 0, len(nums) - 1
    mid = (left + right) // 2
    if left == right:
      return nums[left] if nums[left] > 0 else 0
    # 左边最大值
    left_max = self.maxSubArray(nums[:mid+1])
    # 右边最大值
    right_max = self.maxSubArray(nums[mid+1:])
    # 中间
    # 中间靠左的最大值
    center_left, center_left_max = 0, 0
    temp_index = mid
    while temp_index >= left:
      center_left += nums[temp_index]
      if center_left > center_left_max:
        center_left_max = center_left
      temp_index -= 1
    # 中间靠右的最大值
    center_right, center_right_max = 0, 0
    temp_index = mid + 1
    while temp_index <= right:
      center_right += nums[temp_index]
      if center_right > center_right_max:
        center_right_max = center_right
      temp_index += 1
    return max([left_max, right_max, center_left_max+center_right_max])

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


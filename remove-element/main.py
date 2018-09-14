

class Solution:
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    start = 0
    for i in range(len(nums)):
      if nums[i] != val:
        nums[start] = nums[i]
        start += 1
    return start

if __name__ == "__main__":
  so = Solution()
  # nums = [1, 2, 2, 3, 3, 4, 4]
  # nums = [1]
  # nums = [1, 2, 2, 2]
  # nums = [0,0,1,1,1,2,2,3,3,4]
  nums = [2, 2]
  # nums is passed in by reference. (i.e., without making a copy)
  # nums = [i for i in range(-999, 999)]
  le = so.removeElement(nums, 2)
  # any modification to nums in your function would be known by the caller.
  # using the length returned by your function, it prints the first len elements.
  print(nums[:le])
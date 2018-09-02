class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, item in enumerate(nums):
            try:
                pos = nums.index(target - item, index+1)
            except ValueError:
                continue
            return [index, pos]

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    target = 6
    ret = solution.twoSum(nums, target)
    print(ret)
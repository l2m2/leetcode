class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    target = 6
    ret = solution.twoSum(nums, target)
    print(ret)
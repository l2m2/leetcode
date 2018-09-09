class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        nums = []

        while x > 0:
            nums.append(x % 10)
            x = x // 10
        c = len(nums)
        for i in range(c // 2):
            if nums[i] != nums[c - 1 -i]:
                return False
        return True


if __name__ == "__main__":
    so = Solution()
    print(so.isPalindrome(121))
    print(so.isPalindrome(-121))
    print(so.isPalindrome(10))
    print(so.isPalindrome(1))
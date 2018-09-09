class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev, xx = 0, x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return xx == rev


if __name__ == "__main__":
    so = Solution()
    print(so.isPalindrome(121))
    print(so.isPalindrome(-121))
    print(so.isPalindrome(10))
    print(so.isPalindrome(1))
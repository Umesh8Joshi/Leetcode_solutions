class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        if num[0] == '-':
            return False
        elif num == num[::-1]:
                return True
        return False
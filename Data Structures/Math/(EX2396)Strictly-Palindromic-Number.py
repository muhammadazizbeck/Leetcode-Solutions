class Solution(object):
    def ispalindrome(self,item):
        return item == item[::-1]

    def find_base_num(self,n,b):
        digits = []
        while n:
            digits.append(str(n%b))
            n //= b
        return "".join(digits)

    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for b in range(2,n-1):
            if not self.ispalindrome(self.find_base_num(n,b)):
                return False
        return True
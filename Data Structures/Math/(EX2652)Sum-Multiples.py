class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = 0
        while n>0:
            if n%3 == 0 or n%5==0 or n%7==0:
                curr += n
            n -= 1
        return curr
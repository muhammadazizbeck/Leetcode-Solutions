class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible = []
        ndivisible = []
        while n > 0:
            if n % m == 0:
                divisible.append(n)
            else:
                ndivisible.append(n)
            n -= 1
        return sum(ndivisible)-sum(divisible)
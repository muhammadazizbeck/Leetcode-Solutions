class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        numbers = [9,8,7,6,5,4,3,2,1]
        for number in numbers:
            if str(number) in n:
                return number
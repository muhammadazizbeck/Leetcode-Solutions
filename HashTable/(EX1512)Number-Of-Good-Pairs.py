from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        
        total = 0

        for char,count in freq.items():
            total += (count*(count-1))/2

        return total
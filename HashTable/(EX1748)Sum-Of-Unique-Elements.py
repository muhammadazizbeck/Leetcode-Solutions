from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        freq = Counter(nums)
        for num,count in freq.items():
            if count == 1:
                total += num
            
        return total
from collections import Counter

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        freq = Counter(nums)
        for num,count in freq.items():
            if count == n:
                return num
            else:
                continue
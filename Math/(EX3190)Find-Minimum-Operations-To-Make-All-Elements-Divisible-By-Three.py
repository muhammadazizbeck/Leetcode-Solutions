class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        for num in nums:
            if num % 3 != 0:
                curr += 1
        return curr
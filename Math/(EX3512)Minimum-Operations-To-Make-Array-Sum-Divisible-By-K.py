class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr = 0
        total = sum(nums)
        while total>0:
            if total % k == 0:
                return curr
            else:
                curr += 1
            total -= 1
        return curr
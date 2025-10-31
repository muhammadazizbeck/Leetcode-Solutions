class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in range(max(nums)+2):
            if item not in nums:
                return item
                break
            else:
                continue
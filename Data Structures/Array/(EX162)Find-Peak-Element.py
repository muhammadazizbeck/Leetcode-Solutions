class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 0 if nums[0] > nums[1] else 1

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


        if nums[0] > nums[1]:
            return 0
        else:
            return n - 1
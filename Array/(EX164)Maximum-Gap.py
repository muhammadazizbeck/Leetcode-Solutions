class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        nums.sort()
        max_num = 0
        for i in range(len(nums)-1):
            difference = abs(nums[i+1]-nums[i])
            max_num = max(difference,max_num)
        return max_num
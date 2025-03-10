class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution1
        nums.sort()
        left,right = 0,len(nums)
        while left<right:
            mid = (left+right)//2
            if nums[mid]>mid:
                right = mid
            else:
                left = mid+1
        return left

        solution2
        n = len(nums)
        return (n*(n+1)/2)-sum(nums)
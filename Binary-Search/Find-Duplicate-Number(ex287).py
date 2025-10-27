class Solution(object):
    def findDuplicate(self, nums):
        left, right = 1, len(nums) - 1  # Binary search on range [1, n]

        while left < right:
            mid = (left + right) // 2
            
            count = sum(num <= mid for num in nums)
            
            if count > mid:
                right = mid  
            else:
                left = mid + 1 

        return left 
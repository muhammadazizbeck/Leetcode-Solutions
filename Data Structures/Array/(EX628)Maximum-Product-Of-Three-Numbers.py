class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        
        # Option 1: top 3 largest
        prod1 = nums[-1] * nums[-2] * nums[-3]
        
        # Option 2: two smallest (possibly negative) + largest
        prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)
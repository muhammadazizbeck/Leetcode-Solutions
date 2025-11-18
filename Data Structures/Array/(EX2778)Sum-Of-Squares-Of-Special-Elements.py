class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                total += nums[i-1]**2
            else:
                continue
        return total
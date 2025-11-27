class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        
        # best[r] = smallest prefix sum seen with index % k = r
        best = [float('inf')] * k
        
        best[0] = 0  # prefix before array starts (index 0)
        
        ans = -float('inf')
        
        for i, num in enumerate(nums):
            prefix += num
            r = (i + 1) % k   # IMPORTANT FIX: use index, NOT prefix sum mod
            
            # find best candidate j where j % k == r
            ans = max(ans, prefix - best[r])
            
            # update best prefix for starting index j = i+1
            best[r] = min(best[r], prefix)
        
        return ans

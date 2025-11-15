class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for num in nums:
            if -num in nums:
                return num
            else:
                continue
            
        return -1
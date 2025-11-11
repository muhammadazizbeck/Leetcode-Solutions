class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        start = 1
        consistent = True
        while consistent:
            if k*start not in nums:
                result = k*start
                consistent = False
            else:
                start += 1
            
        return result
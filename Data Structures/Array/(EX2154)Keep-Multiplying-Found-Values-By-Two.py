class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        cycle = 1
        while cycle>0:
            for num in nums:
                if num == original:
                    original = original*2
                    cycle += 1
                else:
                    continue
                
            cycle -= 1
        
        return original
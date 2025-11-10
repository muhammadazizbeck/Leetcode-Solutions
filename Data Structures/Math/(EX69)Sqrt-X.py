class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        pointer = 1
        while pointer*pointer <= x:
            pointer += 1
        return pointer-1
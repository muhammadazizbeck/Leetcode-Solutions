class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if num % 2 == 0:
                result |= num
                count += 1
            else:
                continue
        
        if count == 0:
            return 0
        
        return result
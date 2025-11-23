class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        total = 0
        for num in nums:
            if num == 1:
                total += 1
            else:
                total = 0
                continue
            max_count = max(max_count,total)

        return max_count
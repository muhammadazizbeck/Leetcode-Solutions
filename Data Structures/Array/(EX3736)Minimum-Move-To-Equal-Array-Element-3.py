class Solution:
    def minMoves(self, nums: List[int]) -> int:
        element = max(nums)
        total = 0
        for num in nums:
            total += (element-num)

        return total
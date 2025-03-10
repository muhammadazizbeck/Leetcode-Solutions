class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        value = 0
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if i % 2 == 1:
                value += nums[i]
        return value
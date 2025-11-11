class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        total = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                total += nums[i]
            else:
                total -= nums[i]
        return total
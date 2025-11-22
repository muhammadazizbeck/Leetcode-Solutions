class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        runner = 0
        for i in range(len(nums)):
            runner += nums[i]
            result.append(runner)
        return result
        
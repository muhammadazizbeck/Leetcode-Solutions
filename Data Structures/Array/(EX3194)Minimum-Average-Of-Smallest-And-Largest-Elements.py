class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        result = []
        n = len(nums)
        cycle = n//2
        nums.sort()
        i = 0
        while cycle>0:
            average = (nums[i]+nums[-(i+1)])/2
            result.append(average)
            i += 1
            cycle -= 1
        return min(result)
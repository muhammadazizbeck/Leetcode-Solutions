class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == nums[i]:
                    counter += 1
        return counter
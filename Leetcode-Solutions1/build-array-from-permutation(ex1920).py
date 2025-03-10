class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        txt = []
        for i in range(len(nums)):
            txt.append(nums[nums[i]])
        return txt
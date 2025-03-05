class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        txt = []
        nums.append(nums[0])
        for i in range(len(nums)-1):
            txt.append(abs(nums[i+1]-nums[i]))
        return max(txt)
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        txt = list(set(nums))
        txt.sort()
        if len(nums)>=3:
            return txt[1]
        else:
            return -1
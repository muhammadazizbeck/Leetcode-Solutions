class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        txt = list(set(nums))
        for rts in txt:
            nums.remove(rts)
        return nums
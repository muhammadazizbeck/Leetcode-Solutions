class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        txt = list(set(nums))
        return (sum(nums)-sum(txt))//(len(nums)-len(txt))
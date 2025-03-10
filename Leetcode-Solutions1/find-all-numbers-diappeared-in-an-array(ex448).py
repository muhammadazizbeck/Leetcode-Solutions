class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_set = set(range(1,len(nums)+1))
        txt = list(full_set-set(nums))
        return txt
        
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        txt = []
        for num in nums:
            if nums.count(num)==1:
                txt.append(num)
        return sum(txt)
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        k = 0
        q = 0
        for num in nums:
            if num >= 10:
                k += num
            else:
                q += num
        return k > q or q > k
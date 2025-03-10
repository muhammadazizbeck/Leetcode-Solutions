class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        txt = []
        for num in nums:
            txt.append(num**2)
        txt.sort()
        return txt
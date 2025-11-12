class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        unique = sorted(set(nums),reverse=True)
        return unique[:k]
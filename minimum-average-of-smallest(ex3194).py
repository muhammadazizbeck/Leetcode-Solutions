class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        arr = []
        nums.sort()
        while nums:
            arr.append(nums.pop(0)+nums.pop(-1))
        return (min(arr)/2)
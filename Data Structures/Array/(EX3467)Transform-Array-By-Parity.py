class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 0:
                even.append(0)
            else:
                odd.append(1)

        return even+odd
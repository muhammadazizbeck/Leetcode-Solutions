class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            count = 0
            for item in nums:
                if num > item:
                    count += 1
                else:
                    continue
            result.append(count)

        return result
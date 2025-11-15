class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index,num in enumerate(nums):
            if num == target:
                result.append(index)
            else:
                continue

        if len(result)==0:
            return [-1,-1]
        else:
            return [result[0],result[-1]]
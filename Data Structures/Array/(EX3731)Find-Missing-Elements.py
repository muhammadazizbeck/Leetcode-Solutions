class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        for num in range(min(nums),max(nums)+1):
            if num not in nums:
                result.append(num)
            else:
                continue
            
        return result

        # elements = list(range(min(nums),max(nums)+1))
        # return list(set(elements)-set(nums))
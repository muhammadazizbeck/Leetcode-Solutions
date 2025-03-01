class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        final = [num for num in nums if nums.count(num)>len(nums)/3]
        return list(set(final))
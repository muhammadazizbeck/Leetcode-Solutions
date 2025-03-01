class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        txt = [num for num in nums if num != 0]
        length = len(nums)-len(txt)
        for i in range(length):
            txt.append(0)
        return txt
class Solution(object):
    def searchInsert(self, nums, target: int) -> int:
        index = 0
        if target in nums:
            return nums.index(target)
        else:
            for num in nums:
                if num < target:
                    index += 1
                else:
                    break
                
        return index
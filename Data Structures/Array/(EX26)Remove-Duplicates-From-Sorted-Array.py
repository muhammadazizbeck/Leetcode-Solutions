
class Solution(object):
    def removeDuplicates(self, nums):
        skeleton = nums.copy()
        seen = set()

        for num in skeleton:
            if num in seen:
                nums.remove(num)
            else:
                seen.add(num)
            
        return len(nums)
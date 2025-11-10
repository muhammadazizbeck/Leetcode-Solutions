class Solution(object):
    def removeElement(self, nums, val: int) -> int:
        skeleton = nums.copy()
        seen = set()

        for num in skeleton:
            if num==val:
                nums.remove(num)
            else:
                seen.add(num)
            
        return len(nums)
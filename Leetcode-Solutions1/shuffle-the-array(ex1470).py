class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        txt = []
        rt = len(nums)//2
        for i in range(len(nums)//2):
            txt.append(nums[i])
            txt.append(nums[i+rt])
        return txt
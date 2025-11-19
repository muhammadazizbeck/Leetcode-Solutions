class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        left,right = 0,1

        for num in nums:
            if num > 0:
                ans[left]=num
                left += 2
            else:
                ans[right]=num
                right += 2
        return ans
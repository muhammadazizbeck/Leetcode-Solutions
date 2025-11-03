import heapq

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort(reverse=True)

        # if not nums:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]

        # return (nums[0]-1)*(nums[1]-1)

        max1,max2 = heapq.nlargest(2,nums)
        return (max1-1)*(max2-1)
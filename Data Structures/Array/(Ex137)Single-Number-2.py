class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 3*sum(set(nums))-sum(nums)
        return final//2

        # final = Counter(nums)
        # for num, count in final.items():
        #     if count == 1:
        #         return num

        # nums.sort()
        # for i in range(0,len(nums)-1,3):
        #     if nums[i]!=nums[i+1]:
        #         return nums[i]
        # return nums[-1]
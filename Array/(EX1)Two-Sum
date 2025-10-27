class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Brute Force
        #Time Complexity:O(n2)
        #Space Complexity:O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #     return []


        #Time Complexity:O(n)
        #Space Complexity:O(n)
        seen = {}
        for index, num in enumerate(nums):
            difference = target-num
            if difference in seen:
                return [seen[difference],index]
            seen[num]=index
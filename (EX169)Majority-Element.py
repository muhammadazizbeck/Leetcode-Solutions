class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # final = Counter(nums)
        # for num, count in final.items():
        #     if count>len(nums)/2:
        #         return num
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # result1 = []
        # result2 = []

        # for num in nums1:
        #     if (num not in nums2):
        #         result1.append(num)
            
        # for num in nums2:
        #     if num not in nums1:
        #         result2.append(num)
            
        # return [list(set(result1)),list(set(result2))]

        set1,set2 = set(nums1),set(nums2)

        return [list(set1-set2),list(set2-set1)]
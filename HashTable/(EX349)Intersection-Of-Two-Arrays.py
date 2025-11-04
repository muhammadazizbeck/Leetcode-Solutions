from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # final = []
        # if len(nums1)>len(nums2):
        #     for num in nums2:
        #         if num in nums1:
        #             final.append(num)

        # else:
        #     for num in nums1:
        #         if num in nums2:
        #             final.append(num)
                
        # return list(set(final))

        result = list(set(nums1))+list(set(nums2))

        freq = Counter(result)

        final = []

        for num, count in freq.items():
            if count == 2:
                final.append(num)
            
        return final
from collections import Counter

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        result = list(set(nums1))+list(set(nums2))+list(set(nums3))
        freq = Counter(result)
        total = 0
        final = []

        for num, count in freq.items():
            if count >= 2:
                final.append(num)
            
        return final
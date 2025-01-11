class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k =0
        q =0
        for i in nums1:
            if i in nums2:
                k += 1
        for i in nums2:
            if i in nums1:
                q += 1
        return [k,q]
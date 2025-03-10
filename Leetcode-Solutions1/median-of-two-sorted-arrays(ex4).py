class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        txt = nums1+ nums2
        i = len(txt)
        txt.sort()
        if len(txt) % 2 == 0:
            return (txt[i//2]+txt[i//2-1])/2
        else:
            return txt[i//2]
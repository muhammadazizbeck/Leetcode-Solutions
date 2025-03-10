class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        next_arr = [ar for ar in arr if arr.count(ar)==1]
        if k > len(next_arr):
            return ""
        else:
            return next_arr[k-1]
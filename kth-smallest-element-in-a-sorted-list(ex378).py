class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        txt = []
        for mat in matrix:
            txt += mat
        txt.sort()
        return txt[k-1]
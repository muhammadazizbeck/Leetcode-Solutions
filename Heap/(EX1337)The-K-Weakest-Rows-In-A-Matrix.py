import heapq

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        result = []

        for row in mat:
            result.append(sum(row))

        heap = [(num,index) for index,num in enumerate(result)]
        heapq.heapify(heap)

        final = []
        while k:
            num,index = heapq.heappop(heap)
            final.append(index)

            k -= 1

        return final
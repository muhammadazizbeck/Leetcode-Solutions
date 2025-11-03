class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = []
        for row in matrix:
            result += row
        
        result.sort()
        return result[k-1]

        # heapq.heapify(result)

        # while k>0:
        #     last = heapq.heappop(result)
        #     k -= 1

        # return last
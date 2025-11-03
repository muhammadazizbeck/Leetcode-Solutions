from collections import Counter
import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(heap)

        result = []
        while heap:
            count,char = heapq.heappop(heap)
            result.append(char*(-count))

        return "".join(result)
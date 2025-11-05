class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # total = len(edges)
        # result = []
        # for edge in edges:
        #     result += edge
        
        # freq = Counter(result)

        # for num,count in freq.items():
        #     if count == total:
        #         return num
        #     else:
        #         continue  

        a,b = edges[0]
        c,d = edges[1]

        if a==c or a==d:
            return a
        return b
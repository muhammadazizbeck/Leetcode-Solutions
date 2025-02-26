class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(0,n))
        txt = []
        for edge in edges:
            txt.append(edge[1])
        return list(nodes-set(txt))
        

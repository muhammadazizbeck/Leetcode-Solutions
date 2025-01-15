class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        txt = []
        for row in edges:
            for num in row:
                txt.append(num)
        for i in txt:
            if txt.count(i)==len(edges):
                return i

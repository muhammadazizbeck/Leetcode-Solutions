class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        final = 0

        while len(grid[0])>0:
            max_s = 0
            for sublist in grid:
                sublist.sort()
                max_s = max(max_s,sublist.pop())
            
            final += max_s
        
        return final
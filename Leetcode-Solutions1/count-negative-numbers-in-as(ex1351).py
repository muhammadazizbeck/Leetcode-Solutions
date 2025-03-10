class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for row in grid:
            for i in row:
                if i < 0:
                    counter += 1
        return counter
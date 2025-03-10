class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        txt = []
        missing = 0
        for gr in grid:
            txt += gr
        txt.sort() 
        for i in range(1,max(txt)):
            if i not in txt:
                missing = i
        rt = [x for x in txt if txt.count(x)==2]
        return [rt[0],missing if  missing != 0 else max(txt)+1]
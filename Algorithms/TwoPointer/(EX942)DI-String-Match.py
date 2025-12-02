class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left,right = 0,len(s)
        result = []
        for char in s:
            if char=="I":
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
            
        result.append(left)
        return result
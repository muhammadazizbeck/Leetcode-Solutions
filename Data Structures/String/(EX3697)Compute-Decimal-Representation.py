class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        initial = 1
        result = []
        leng = len(str(n))

        while leng>0:
            extra = n % (10**initial)
            if extra != 0:
                result.append(extra)
            
            initial += 1

            n = n - extra

            leng -= 1
        
        return sorted(result,reverse=True)
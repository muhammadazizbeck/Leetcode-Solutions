class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        elem,count=freq.most_common(1)[0]
        
        for item,total in freq.items():
            if total != count:
                return False
            else:
                continue
            
        return True
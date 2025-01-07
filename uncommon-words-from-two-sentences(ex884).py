class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        rt = []
        txt = s1.split() + s2.split()
        for i in txt:
            if txt.count(i)==1:
                rt.append(i)
        return rt
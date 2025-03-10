class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        txt1,txt2 = "",""
        for i in word1:
            txt1 += i
        for j in word2:
            txt2 += j
        if txt1 == txt2:
            return True
        else:
            return False
class Solution:
    def sortSentence(self, s: str) -> str:
        final = s.split()
        result = sorted(final,key=lambda x:x[-1])

        return " ".join(char[:-1:] for char in result)
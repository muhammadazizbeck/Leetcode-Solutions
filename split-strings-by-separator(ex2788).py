class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        txt = []
        for word in words:
            parts = word.replace(separator," ")
            finals  = parts.split()
            for final in finals:
                txt.append(final)
        return txt
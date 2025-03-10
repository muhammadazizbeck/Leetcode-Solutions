class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_num = 0
        for word in words:
            if pref == word[0:len(pref)]:
                pref_num += 1
        return pref_num
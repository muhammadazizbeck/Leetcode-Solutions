class Solution:
    def minimizedStringLength(self, s: str) -> int:
        txt = []
        for i in s:
            txt.append(i)
        return len(list(set(txt)))
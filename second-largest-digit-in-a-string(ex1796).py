class Solution:
    def secondHighest(self, s: str) -> int:
        txt = [int(i) for i in s if i.isdigit()]
        if len(set(txt)) < 2:
            return -1
        return sorted(list(set(txt)),reverse=True)[1]
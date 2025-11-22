class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for char in s:
            if char.isdigit() and char not in seen:
                seen.add(char)
            else:
                continue

        if len(seen)<=1:
            return -1
        else:
            liss = sorted(seen,reverse=True)
            return int(liss[1])
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        xr = s.count(letter)
        return floor(xr/len(s)*100)
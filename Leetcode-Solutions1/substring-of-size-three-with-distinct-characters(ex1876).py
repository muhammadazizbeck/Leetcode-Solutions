class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == len(list(s[i:i+3])):
                counter += 1
        return counter 
        
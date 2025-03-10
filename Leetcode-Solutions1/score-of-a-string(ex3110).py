class Solution:
    def scoreOfString(self, s: str) -> int:
        even_sum = 0
        for i in range(len(s)-1):
            even_sum += abs(ord(s[i])-ord(s[i+1]))
        return even_sum
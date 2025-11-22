class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = ""
        first = 96
        for char in s:
            total += str(ord(char)-first)
        
        while k>0:
            total = sum(int(char) for char in str(total))
            k -= 1
        
        return int(total)
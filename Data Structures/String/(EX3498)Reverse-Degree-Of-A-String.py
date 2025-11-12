class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        count = 1
        for char in s:
            total += count*(27-(ord(char)-96))
            count += 1
        return total
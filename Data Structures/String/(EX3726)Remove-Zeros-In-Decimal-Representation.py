class Solution:
    def removeZeros(self, n: int) -> int:
        result = ""
        for char in str(n):
            if char != "0":
                result += char
        return int(result)
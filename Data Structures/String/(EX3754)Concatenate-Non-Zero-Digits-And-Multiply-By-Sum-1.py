class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(char) for char in str(n) if char != "0"]

        if not digits:      
            return 0

        key = int("".join(str(d) for d in digits))
        return key * sum(digits)
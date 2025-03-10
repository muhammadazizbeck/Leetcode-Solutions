class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n > 10:
            return 0

        count = 0
        for length in range(0, n + 1):
            count += 9 * factorial(9) // factorial(10 - length)
        return count+1
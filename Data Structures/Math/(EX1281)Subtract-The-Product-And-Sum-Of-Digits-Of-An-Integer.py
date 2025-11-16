class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(char) for char in str(n)]
        total = 1
        for digit in digits:
            total *= digit

        return total-sum(digits)
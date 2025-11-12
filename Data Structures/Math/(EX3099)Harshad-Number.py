class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        result = [int(char) for char in str(x)]

        if x % sum(result) == 0:
            return sum(result)
        else:
            return -1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        areg = num ** (1/2)
        return areg.is_integer()
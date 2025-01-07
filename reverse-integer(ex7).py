class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num

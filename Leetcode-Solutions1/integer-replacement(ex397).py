class Solution:
    def integerReplacement(self, n: int) -> int:
        counter = 0
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            elif n == 3 or (n-1)%4 == 0:
                n -= 1
            else:
                n += 1
            counter += 1
        return counter
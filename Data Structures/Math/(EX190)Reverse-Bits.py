class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        reversed_bits = b[::-1]
        return int(reversed_bits, 2)
class Solution:
    def hammingWeight(self, n: int) -> int:
        final = bin(n)[2:]

        return final.count("1")
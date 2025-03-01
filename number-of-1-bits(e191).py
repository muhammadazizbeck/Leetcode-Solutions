class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        tr = bin(n)[2:]
        for i in str(tr):
            if i == '1':
                count += 1
        return count
        
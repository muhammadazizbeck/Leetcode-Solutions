class Solution:
    def countBits(self, n: int) -> List[int]:
        txt = []
        txt2 = []
        for i in range(n+1):
            txt.append(bin(i)[2:])
        for tx in txt:
            txt2.append(tx.count('1'))
        return txt2
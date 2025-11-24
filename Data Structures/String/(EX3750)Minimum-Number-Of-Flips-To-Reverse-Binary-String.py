class Solution:
    def minimumFlips(self, n: int) -> int:
        repr = bin(n)[2:]
        rrepr = repr[::-1]
        count = 0

        for index in range(len(repr)):
            if repr[index]!=rrepr[index]:
                count += 1
            else:
                continue
            
        return count
class Solution:
    def findComplement(self, num: int) -> int:
        txt = bin(num)[2:]
        val = ''
        for i in txt:
            if i == '1':
                val += '0'
            else:
                val += '1'
        return int(val,2)
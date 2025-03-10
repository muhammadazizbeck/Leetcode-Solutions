class Solution:
    def reverseWords(self, s: str) -> str:
        rte = s.split()[::-1]
        count = ''
        for ert in rte:
            count += ert
            count += ' '
        return count.rstrip()
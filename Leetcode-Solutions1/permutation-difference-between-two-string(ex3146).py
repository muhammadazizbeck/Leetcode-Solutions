class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        txt = []
        for x in s:
            txt.append(abs(s.index(x)-t.index(x)))
        return sum(txt)
        
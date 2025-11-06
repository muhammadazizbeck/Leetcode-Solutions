class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        n = len(s)
        for i in range(n-1):
            total += abs(ord(s[i])-ord(s[i+1]))
        return total
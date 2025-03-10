class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = sorted(s, reverse=True)  # Sort in descending order
        seen = set(s)

        for ch in s:
            if ch.isupper() and ch.lower() in seen:
                return ch
        
        return ""
        
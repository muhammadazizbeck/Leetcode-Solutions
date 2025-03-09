class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        inside = False
        for char in s:
            if char == '|':
                inside = not inside
            elif char == "*" and not inside:
                counter += 1
        return counter
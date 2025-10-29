class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(list(stack))
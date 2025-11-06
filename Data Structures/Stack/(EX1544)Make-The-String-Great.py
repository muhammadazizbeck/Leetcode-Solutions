class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack:
                top = stack[-1]
                if top.isupper() and char==top.lower():
                    stack.pop()
                    continue
                if top.islower() and char==top.upper():
                    stack.pop()
                    continue
            stack.append(char)
        return "".join(list(stack))
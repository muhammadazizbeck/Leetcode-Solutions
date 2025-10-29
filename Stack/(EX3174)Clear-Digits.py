class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = []
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return "".join(list(stack))
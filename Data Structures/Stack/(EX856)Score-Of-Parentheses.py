class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1]+=max(2*val,1)
        return stack.pop()
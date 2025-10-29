class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        aver = 0
        maxi = 0
        for char in s:
            if char == "(":
                aver += 1
                maxi = max(aver,maxi)
            elif char == ")":
                aver -= 1
            else:
                continue
        return maxi

        # stack = []
        # maxi = 0

        # for char in s:
        #     if char == "(":
        #         stack.append(char)
        #         maxi = max(maxi, len(stack))
        #     if char == ")":
        #         stack.pop()
        # return maxi
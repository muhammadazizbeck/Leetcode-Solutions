class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        # total = 0
        # for log in logs:
        #     if log == "../":
        #         if total>0:
        #             total -= 1
        #     elif log == "./":
        #         continue
        #     else:
        #         total += 1

        # return total

        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)
        return len(stack)
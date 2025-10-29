class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in ops:
            if op == "C":
                if stack:
                    stack.pop()
            elif op == 'D':
                if stack:
                    stack.append(2*int(stack[-1]))
            elif op == '+':
                if len(stack)>=2:
                    stack.append(int(stack[-2]+int(stack[-1])))
                elif len(stack)==1:
                    stack.append(int(stack[-1]))
            else:
                stack.append(int(op))
        return sum(stack)
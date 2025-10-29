class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # while 'AB' in s or "CD" in s:
        #     s = s.replace("AB","",1)
        #     s = s.replace("CD","",1)
        # return len(s)
        
        stack = []

        for char in s:
            if stack:
                top = stack[-1]
                if (top=="A" and char=="B") or (top=="C" and char=="D"):
                    stack.pop()
                    continue
            stack.append(char)
        return len(stack)
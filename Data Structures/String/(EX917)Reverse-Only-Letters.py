class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [char for char in s if char.isalpha()]
        result = []
        for item in s:
            if item.isalpha():
                result.append(stack.pop())
            else:
                result.append(item)

        return "".join(result)
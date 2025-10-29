class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        if index == -1:
            return word
        return word[:index+1][::-1]+word[index+1:]

        # stack = []
        # for index, char in enumerate(word):
        #     stack.append(char)
        #     if char == ch:
        #         reversed_part = "".join(reversed(stack))
        #         remaining_part = word[index+1:]
        #         return reversed_part+remaining_part
        # return word
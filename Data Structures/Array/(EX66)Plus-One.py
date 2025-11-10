class Solution(object):
    def plusOne(self, digits):
        
        num = ""
        for digit in digits:
            num += str(digit)

        final = int(num)+1

        return [int(char) for char in str(final)]
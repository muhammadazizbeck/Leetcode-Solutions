class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        divided = s.split()
        if len(divided)==0:
            return 0
        return len(divided[-1])
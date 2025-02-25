class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0
        words = text.split() 
        for word in words:
            if len(set(word) - set(brokenLetters)) == len(set(word)):  
                counter += 1
        return counter

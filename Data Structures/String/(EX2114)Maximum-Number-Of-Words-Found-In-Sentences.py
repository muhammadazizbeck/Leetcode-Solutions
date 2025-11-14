class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # lengths = [len(word.split()) for word in sentences]

        # return max(lengths)

        max_size = 0
        for sentence in sentences:
            words = sentence.split()
            max_size = max(max_size,len(words))
        
        return max_size
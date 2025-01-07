class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexs = []
        for idx,word in enumerate(words):
            if x in word:
                indexs.append(idx)
        return indexs
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_withs = []
        for sentence in sentences:
            trt = len(sentence.split())
            max_withs.append(trt)
        return max(max_withs)
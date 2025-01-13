class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_dict = {int(word[-1]): word[:-1] for word in words}
        return ' '.join(word_dict[i] for i in sorted(word_dict.keys()))
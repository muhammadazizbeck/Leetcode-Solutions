from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        first = s1.split()
        second = s2.split()
        result = first+second
        freq = Counter(result)
        final = []
        for word,count in freq.items():
            if count == 1:
                final.append(word)
            
        return final
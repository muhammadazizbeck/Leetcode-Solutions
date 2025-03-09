class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final_val = ""
        min_length = min(len(word1),len(word2))
        for i in range(min_length):
            final_val += word1[i]
            final_val += word2[i]
        if len(word1)>len(word2):
            final_val += word1[min_length:]
        else:
            final_val += word2[min_length:]
        return final_val
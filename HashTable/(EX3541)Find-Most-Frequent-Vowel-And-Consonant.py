from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        freq = Counter(s)

        vowel_max,consonant_max=0,0

        for char, count in freq.items():
            if char in vowels:
                vowel_max = max(vowel_max,count)
            else:
                consonant_max = max(consonant_max,count)
            
        return vowel_max + consonant_max
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # total = 0

        # freq = Counter(sentence)
        # for char, count in freq.items():
        #     if count >= 1:
        #         total += 1
            
        
        # return total >= 26

        return len(set(sentence))==26
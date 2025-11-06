class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        # total = 0

        # for word in words:
        #     if set(word).issubset(allowed):
        #         total += 1
            
        # return total

        set_all = set(allowed)
        total = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in set_all:
                    consistent = False
                    break
            if consistent:
                total += 1

        return total
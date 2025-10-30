from collections import Counter
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        final = Counter(nums)
        for num, count in final.items():
            if count >= 2:
                result.append(num)
        return result
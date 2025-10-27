class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        val = []
        final = Counter(nums)
        for num, count in final.items():
            if count > len(nums)/3:
                val.append(num)
        return val
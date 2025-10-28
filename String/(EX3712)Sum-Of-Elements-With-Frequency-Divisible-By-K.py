class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val = 0
        final = Counter(nums)
        for num, count in final.items():
            if count % k == 0:
                val += count*num
        return val
import heapq

class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)//2
        heapq.heapify(nums)
        bob = []
        alice = []
        final = []

        while nums:
            alice.append(heapq.heappop(nums))
            bob.append(heapq.heappop(nums))

        for i in range(n):
            final.append(bob[i])
            final.append(alice[i])

        return final
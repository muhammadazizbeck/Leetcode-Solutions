import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = [] 
        result = []


        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))


        result.append(-heap[0][0])


        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))


            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            result.append(-heap[0][0])

        return result
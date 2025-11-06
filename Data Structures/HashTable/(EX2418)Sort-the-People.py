class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        heap = list(zip(names,heights))
        heap.sort(key=lambda x:x[1],reverse=True)

        return [name for name, height in heap]
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        final_names = [name for _,name in sorted(zip(heights,names),reverse=True)]
        return final_names
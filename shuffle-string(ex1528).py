class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        letters = []
        for x in s:
            letters.append(x) 
        sorted_list = [letter for _,letter in sorted(zip(indices,letters))]
        final_val = ""
        for rt in sorted_list:
            final_val += rt
        return final_val
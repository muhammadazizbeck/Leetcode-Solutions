class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        val = 0
        x = len(num)-1
        for n in num:
            val += n*(10**x)
            x -= 1
        final_list = []
        total = val + k
        for i in str(total):
            final_list.append(int(i))
        return final_list
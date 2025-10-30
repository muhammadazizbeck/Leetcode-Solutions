class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        snum = str(num)
        if "6" in snum:
            final = snum.replace("6","9",1)
        else:
            final = snum
        return int(final)
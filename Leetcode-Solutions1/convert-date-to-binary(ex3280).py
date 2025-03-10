class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        txt = date.split("-")
        final_str = ""
        for tx in txt:
            final_str += bin(int(tx))[2:]
            final_str += "-"
        return final_str[:-1]

        
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        binaries = []
        date.split('-')
        
        for cre in date:
            binaries.append(bin(cre)[2:])
        return "-".join(binaries())
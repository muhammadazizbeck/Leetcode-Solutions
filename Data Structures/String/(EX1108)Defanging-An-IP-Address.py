class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # curr = ""
        # for char in address:
        #     if char != ".":
        #         curr += char
        #     else:
        #         curr += "[.]"
        # return curr

        final = address.replace(".","[.]")
        return final
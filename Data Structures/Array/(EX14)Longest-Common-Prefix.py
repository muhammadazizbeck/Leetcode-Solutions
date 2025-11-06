class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # strs.sort()
        # first_str = strs[0]
        # last_str = strs[-1]
        # min_length = min(len(first_str),len(last_str))
        # i = 0
        # while i<min_length and first_str[i]==last_str[i]:
        #     i += 1
        # return first_str[:i]


        if not strs:
            return ""
        prefix = strs[0]
        for item in strs[1:]:
            while not item.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    ""
        return prefix


        # if not strs:
        #     return ""

        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != char:
        #             return strs[0][:i]
        # return strs[0]
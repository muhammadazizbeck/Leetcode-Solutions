class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first = len(haystack)
        second = len(needle)

        if second>first:
            return -1

        for index in range(first-second+1):
            if haystack[index:index+second]==needle:
                return index

        return -1
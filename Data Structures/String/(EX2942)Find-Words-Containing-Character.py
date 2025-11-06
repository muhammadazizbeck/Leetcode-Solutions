class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        curr = 0
        for operation in operations:
            if "-" in operation:
                curr -= 1
            else:
                curr += 1
        return curr
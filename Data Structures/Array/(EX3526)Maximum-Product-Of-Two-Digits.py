class Solution:
    def maxProduct(self, n: int) -> int:
        result = [int(char) for char in str(n)]
        result.sort(reverse=True)

        if len(result)<2:
            return sum(result)

        return result[0]*result[1]
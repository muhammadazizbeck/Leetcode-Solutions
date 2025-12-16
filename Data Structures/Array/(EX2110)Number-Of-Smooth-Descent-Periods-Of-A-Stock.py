class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 0
        length = 0

        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1

            result += length

        return result

       
       # some line of code
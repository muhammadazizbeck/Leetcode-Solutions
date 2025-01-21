class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        txt = []
        for num in candies:
            if (num + extraCandies)>=max(candies):
                txt.append(True)
            else:
                txt.append(False)
        return txt
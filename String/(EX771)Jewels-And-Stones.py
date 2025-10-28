from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        total = 0
        seen = set()
        final = Counter(stones)

        for stone, count in final.items():
            if stone in jewels and stone not in seen:
                total += count
            seen.add(stone)
        return total
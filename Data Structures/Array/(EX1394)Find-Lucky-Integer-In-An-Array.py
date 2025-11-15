class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        max_lucky = float("-inf")

        for num,count in freq.items():
            if num == count:
                max_lucky = max(max_lucky,num)
            else:
                continue

        if max_lucky != float("-inf"):
            return max_lucky
        else:
            return -1

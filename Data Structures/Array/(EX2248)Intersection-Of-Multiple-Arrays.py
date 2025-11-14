class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        result = []
        final = []
        for num in nums:
            result += num

        freq = Counter(result)

        for char,count in freq.items():
            if count >= n:
                final.append(char)
            else:
                continue

        final.sort()

        return final
class Solution:
    def minElement(self, nums: List[int]) -> int:
        txt = []
        for num in nums:
            sum = 0
            for i in str(num):
                sum += int(i)
            txt.append(sum)
        return min(txt)
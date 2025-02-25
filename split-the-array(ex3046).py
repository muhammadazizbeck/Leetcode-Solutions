class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        txt = []
        for number,index in counter.items():
            txt.append(counter[number])
        txt.sort(reverse=True)
        if txt[0] >= 3:
            return False
        else:
            return True
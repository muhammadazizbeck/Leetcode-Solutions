class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])                 # 0, 2, 4, ... indekslar
        odd = sorted(nums[1::2], reverse=True)   # 1, 3, 5, ... indekslar

        result = []
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even[e])
                e += 1
            else:
                result.append(odd[o])
                o += 1
        return result

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         final = [num for num in nums if nums.count(num)>len(nums)/3]
#         return list(set(final))

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        txt = [key for key,val in counter.items() if val>n//3]
        return txt
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list = [num for num in nums if num % 2 == 0]
        odd_list = [num for num in nums if num % 2 == 1]
        return even_list+odd_list

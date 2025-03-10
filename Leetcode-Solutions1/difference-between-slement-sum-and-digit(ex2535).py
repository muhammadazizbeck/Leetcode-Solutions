class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        counter = []
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(abs(num)))
            counter.append(digit_sum)
        return abs(sum(nums)-sum(counter))
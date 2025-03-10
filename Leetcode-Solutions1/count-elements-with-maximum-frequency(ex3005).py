class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        final_list = []
        count = 0
        for number,index in counter.items():
            final_list.append(counter[number])
        final_list.sort(reverse=True)
        for x in final_list:
            if x == final_list[0]:
                count += x
            else:
                break
        return count
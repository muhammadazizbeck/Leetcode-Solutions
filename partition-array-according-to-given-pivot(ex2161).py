class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_list = []
        right_list = []
        count = 0
        for num in nums:
            if num < pivot:
                left_list.append(num)
            elif num > pivot:
                right_list.append(num)
            else:
                count += 1
        for_pivot = []
        for i in range(count):
            for_pivot.append(pivot)
        return left_list+for_pivot+right_list
        
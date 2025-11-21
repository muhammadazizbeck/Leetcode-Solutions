class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # seen = set()

        # for num in arr:
        #     if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
        #         return True
        #     seen.add(num)

        # return False

        arr.sort()

        for i in range(len(arr)):
            target = arr[i] * 2
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target and mid != i:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
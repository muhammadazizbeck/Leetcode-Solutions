class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum_num = 0
        for num in operations:
            if num == "--X" or num == "X--":
                sum_num -= 1
            if num == "++X" or num == "X++":
                sum_num += 1
        return sum_num
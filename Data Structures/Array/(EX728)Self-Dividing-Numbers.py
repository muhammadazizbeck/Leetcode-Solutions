class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_divident(item):
            nums = [int(char) for char in str(item)]
            for num in nums:
                if num == 0:
                    return False
                if item % num != 0:
                    return False
                else:
                    continue
            return True

        result = []
        for rt in range(left,right+1):
            if is_self_divident(rt):
                result.append(rt)
            else:
                continue
            
        return result
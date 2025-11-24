class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        total = ""
        result = []
        for num in nums:
            total += str(num)
            if int(total,2) % 5 == 0:
                result.append(True)
            else:
                result.append(False)
                
        return result
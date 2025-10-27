class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index,num in enumerate(numbers):
            difference = target-num
            if difference in seen:
                return [seen[difference]+1,index+1]
            seen[num]=index
        return []
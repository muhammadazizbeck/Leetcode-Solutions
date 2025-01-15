class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #1
        # txt=[]
        # for i in range(len(nums)):
        #     txt.append(sum(nums[:i+1]))
        # return txt
        txt = []
        counter = 0
        for num in nums:
            counter += num
            txt.append(counter)
        return txt
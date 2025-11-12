class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True

        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1])%2==0:
                return False
                break
            else:
                continue
            
        return True
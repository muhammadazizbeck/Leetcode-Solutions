class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(set(nums))!=len(nums)

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False

        # final = Counter(nums)
        # for num, count in final.items():
        #     if count >= 2:
        #         return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
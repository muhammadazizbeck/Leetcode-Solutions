class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        counts = Counter(nums) 
        for num, count in counts.items():
            if count > 1:
                duplicates.append(num)
        return duplicates
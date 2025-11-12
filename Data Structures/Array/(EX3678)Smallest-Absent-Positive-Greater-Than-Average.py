class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1

        if max(nums)<=0:
            return 1                   

        total = sum(nums)
        avg = total / n                  

        
        positives = set()
        for x in nums:
            if x > 0:
                positives.add(x)

        
        candidate = int(avg) + 1         
        while True:
            if candidate not in positives and candidate>0:
                return candidate
            candidate += 1
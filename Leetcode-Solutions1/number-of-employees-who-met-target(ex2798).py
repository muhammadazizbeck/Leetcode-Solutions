class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        numb = 0
        hours.sort(reverse=True)
        for hour in hours:
            if hour >= target:
                numb += 1
        return numb
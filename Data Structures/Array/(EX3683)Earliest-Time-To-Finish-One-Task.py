class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        duration = sum(tasks[0])
        for task in tasks:
            duration = min(duration,sum(task))

        return duration
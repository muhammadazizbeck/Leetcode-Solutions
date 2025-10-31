from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while students and count<len(students):
            if students[0]==sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students.popleft())
                count += 1
        return len(students)
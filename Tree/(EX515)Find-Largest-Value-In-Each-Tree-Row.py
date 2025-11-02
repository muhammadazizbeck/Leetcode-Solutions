# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        result = []

        queue = deque([root])

        while queue:
            level_max = float("-inf")

            for _ in range(len(queue)):
                curr = queue.popleft()
                level_max = max(level_max,curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(level_max)
        
        return result
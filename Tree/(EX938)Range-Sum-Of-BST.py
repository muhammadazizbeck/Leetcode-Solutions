# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        
        if not root:
            return 0

        queue = deque([root])
        total = 0

        while queue:
            curr = queue.popleft()
            if not curr:
                continue

            if low<=curr.val<=high:
                total += curr.val
            
            if curr.left and curr.val>low:
                queue.append(curr.left)
            
            if curr.right and curr.val<high:
                queue.append(curr.right)

        return total

        # if not root:
        #     return 0
        
        # total = 0

        # if low<=root.val<=high:
        #     total += root.val

        # if root.val > low:
        #     total += self.rangeSumBST(root.left,low,high)
        
        # if root.val < high:
        #     total += self.rangeSumBST(root.right,low,high)

        # return total
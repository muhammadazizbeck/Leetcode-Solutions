# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        seen = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val not in seen:
                seen.add(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        final = list(seen)

        if len(final)<2:
            return -1
        else:
            return sorted(final)[1]
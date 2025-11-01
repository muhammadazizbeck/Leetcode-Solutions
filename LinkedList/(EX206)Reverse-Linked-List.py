# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if not head:
        #     return None

        # curr = head
        # stack = []
        
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next
  
        # newnode = stack.pop()
        # curr = newnode
        # while stack:
        #     curr.next = stack.pop()
        #     curr = curr.next

        # curr.next = None
        # return newnode

        prev = None
        curr = head

        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev
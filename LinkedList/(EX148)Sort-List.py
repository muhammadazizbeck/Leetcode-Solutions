# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        curr = head
        
        while curr:
            result.append(curr.val)
            curr = curr.next
        
        result.sort()

        final = ListNode(0)
        curr = final

        for item in result:
            curr.next = ListNode(item)
            curr = curr.next
        return final.next
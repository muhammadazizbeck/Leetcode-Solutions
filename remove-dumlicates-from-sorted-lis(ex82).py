# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        txt = [only for only in values if values.count(only)==1]
        dummy = ListNode()
        current = dummy
        for rt in txt:
            current.next = ListNode(rt)
            current = current.next
        return dummy.next
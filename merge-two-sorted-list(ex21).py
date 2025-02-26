# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr1 = list1
        curr2 = list2
        while curr1:
            values.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            values.append(curr2.val)
            curr2 = curr2.next
        values.sort()
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
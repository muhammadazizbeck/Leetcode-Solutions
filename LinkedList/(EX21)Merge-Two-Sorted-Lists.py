# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        curr1 = list1
        while curr1:
            result.append(curr1.val)
            curr1 = curr1.next
        
        curr2 = list2
        while curr2:
            result.append(curr2.val)
            curr2 = curr2.next

        result.sort()

        helper = ListNode(0)
        curr = helper

        for item in result:
            curr.next = ListNode(item)
            curr = curr.next
        return helper.next
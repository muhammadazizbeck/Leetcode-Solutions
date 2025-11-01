# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        result = []

        for list0 in lists:
            curr = list0
            while curr:
                result.append(curr.val)
                curr = curr.next
        
        result.sort()

        helper = ListNode(0)
        curr = helper

        for item in result:
            curr.next = ListNode(item)
            curr = curr.next

        return helper.next
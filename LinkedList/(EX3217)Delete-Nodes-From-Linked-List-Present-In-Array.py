# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        short = set(nums)
        helper = ListNode(0)
        helper.next = head
        current = helper

        while current.next is not None:
            if current.next.val in short:
                current.next = current.next.next
            else:
                current = current.next
        return helper.next
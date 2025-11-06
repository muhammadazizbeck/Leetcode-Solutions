# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # final = ""
        # curr = head
        # while curr:
        #     final += str(curr.val)
        #     curr = curr.next
        # return final == final[::-1]

        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True
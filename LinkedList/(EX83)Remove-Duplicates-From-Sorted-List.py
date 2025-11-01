# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

        # if not head:
        #     return None

        # seen = set()
        # queue = deque()

        # curr = head

        # while curr:
        #     if curr.val not in seen:
        #         queue.append(curr.val)
        #         seen.add(curr.val)
        #     curr = curr.next
        
        # new_head = ListNode(queue.popleft())
        # curr = new_head

        # while queue:
        #     curr.next = ListNode(queue.popleft())
        #     curr = curr.next
        
        # return new_head
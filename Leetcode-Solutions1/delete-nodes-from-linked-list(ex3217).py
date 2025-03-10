# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        curr = dummy  
        set_nums = set(nums)
        while curr and curr.next:
            if curr.next.val in set_nums:
                curr.next = curr.next.next  
            else:
                curr = curr.next  # Faqat keyingi tugunga o‘tamiz

        return dummy.next

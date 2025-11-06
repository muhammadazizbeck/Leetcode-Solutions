import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        current = head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        while current and current.next:
            g = gcd(current.val, current.next.val)
            new_node = ListNode(g)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        return head
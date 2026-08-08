# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        we can do a recursion, or just iteration
        # bruuuuh i did in incorrect order i should've started from left, and started reversing from left to right 
        """
        if head is None or right == left: return head

        dummy = ListNode(0, head)

        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        tail = curr

        prevN = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prevN
            prevN = curr
            curr = tmp
        
        prev.next = prevN
        tail.next = curr

        return dummy.next
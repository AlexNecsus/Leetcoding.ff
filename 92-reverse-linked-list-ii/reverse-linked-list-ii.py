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
        
        prev = dummy # first of left
        # Move to node before reversal
        for _ in range(left - 1):
            prev = prev.next 

        # Start reversal
        curr = prev.next # 2
        tail = curr # Track tail as the original first node of the segment , (2)
        
        # Reverse the sublist
        prevN = None # 2 -> 3 -> 4
        for _ in range(right - left + 1): # Include ALL nodes
            tmp = curr.next
            curr.next = prevN
            prevN = curr
            curr = tmp # 3 -> 4 -> 5
        
        # Reconnect list
        prev.next = prevN # 1 => 4 # prev_node is the new head of reversed segment
        tail.next = curr # 2 => 5 # Connect tail to the rest of the list

        return dummy.next # 1->....
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        
        return newhead

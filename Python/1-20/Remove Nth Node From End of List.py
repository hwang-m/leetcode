# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

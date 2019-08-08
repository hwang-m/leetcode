# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        # split into two lists: head and second, and sort each
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = self.sortList(slow.next)
        slow.next = None
        head = self.sortList(head)
        
        return self.mergeLists(head, second)
        
        
    def mergeLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not (head1 and head2):
            return head1 or head2
        
        if head1.val > head2.val:
            newhead = head2
            head2 = head2.next
        else:
            newhead = head1
            head1 = head1.next
        
        pre = newhead
        while head1 and head2:
            if head1.val > head2.val:
                pre.next = head2
                head2 = head2.next
            else:
                pre.next = head1
                head1 = head1.next
            pre = pre.next
        
        pre.next = head1 or head2
        return newhead

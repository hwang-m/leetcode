# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        dummy = pre = ListNode(float('-inf'))
        
        while head:
            if pre.val > head.val:
                pre = dummy
            while pre.next and pre.next.val < head.val:
                pre = pre.next
            temp = head.next
            head.next = pre.next
            pre.next = head
            head = temp
        
        return dummy.next

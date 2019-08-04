# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        while head and head.next:
            if head.val != head.next.val:
                pre = head
                head = head.next
            else:
                while head and head.val == pre.next.val:
                    head = head.next
                pre.next = head
				
        return dummy.next

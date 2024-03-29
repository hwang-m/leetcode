# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        l1.val += l2.val
        
        if l1.val < 10:
            l1.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l1.val = l1.val % 10
            l1.next = self.addTwoNumbers(self.addTwoNumbers(l1.next, l2.next), ListNode(1))
        
        return l1

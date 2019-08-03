# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        # find the length n and connect the end node to the head
        node = head
        n = 1
        while node.next:
            node = node.next
            n += 1
        node.next = head
        
        # find the new end node
        k = n - k % n
        for _ in range(k):
            node = node.next
        
        node.next, node= None, node.next
        return node

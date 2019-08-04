# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            slow.next = fast
            if fast:
                slow, fast = fast, fast.next
        return head

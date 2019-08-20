# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not (head and head.next):
            return True
        slow = fast = head
        slow_pos = head.next
        slow_pre = None
        while fast and fast.next:
            fast = fast.next.next
            # reverse the first half
            slow.next = slow_pre
            slow_pre, slow, slow_pos = slow, slow_pos, slow_pos.next
        if fast:
            slow = slow.next
        # compare the second half to the reversed first half
        while slow and slow.val == slow_pre.val:
            slow = slow.next
            slow_pre = slow_pre.next
        return not slow

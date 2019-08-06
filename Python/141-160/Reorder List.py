class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # make sure 'fast.next' and 'second.next' (defined below) exist
        if not (head and head.next):
            return
        
        # split into two lists
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        # reverse second list
        pre = None
        while second and second.next:
            pos = second.next
            second.next = pre
            pre = second
            second = pos
        second.next = pre
        
        # merge two lists
        cur = head
        while cur and cur.next:
            temp1 = cur.next
            cur.next = second
            temp2 = second.next
            second.next = temp1
            second = temp2
            cur = temp1
        cur.next = second

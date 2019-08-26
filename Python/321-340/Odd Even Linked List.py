# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if number of nodes < 3: return head
        # otherwise:
        if head and head.next and head.next.next:
            even = evenhead = ListNode(0)
            odd = head
            while odd.next:
                even.next = odd.next
                even = even.next
                odd.next = even.next
                if odd.next:
                    odd = odd.next
                else:
                    break
            even.next = None
            odd.next = evenhead.next
        return head

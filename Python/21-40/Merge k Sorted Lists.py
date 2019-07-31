# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return lists
        
        def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
            node = dummy_head = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            if l1:
                node.next = l1
            else:
                node.next = l2
            return dummy_head.next
        
        for i in range(1, len(lists)):
            lists[i] = merge_two_lists(lists[i - 1], lists[i])
        return lists[-1]

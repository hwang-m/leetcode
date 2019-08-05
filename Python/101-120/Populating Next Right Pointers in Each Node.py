"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        newroot = root
        while newroot:
            node = newroot
            while node:
                if node.left:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
                    node = node.next
                else:
                    break
            newroot = newroot.left
        return root

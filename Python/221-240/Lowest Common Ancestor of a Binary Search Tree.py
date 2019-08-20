# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rval = root.val
        pval = p.val
        qval = q.val
        # assume pval and qval both exist and are different
        # if they are both less than rval, LCA is in the left subtree
        if pval < rval and qval < rval: return self.lowestCommonAncestor(root.left, p, q)
        # if they are both greater than rval, LCA is in the right subtree
        if pval > rval and qval > rval: return self.lowestCommonAncestor(root.right, p, q)
        # if they are in different subtrees, or one of them is the root, then LCA is the root
        return root

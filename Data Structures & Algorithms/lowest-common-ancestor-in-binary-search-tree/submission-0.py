# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        nodes = {p, q}
        return self._lca(root, nodes)

    def _lca(self, root: TreeNode, nodes: set[TreeNode]) -> TreeNode | None:
        if not root:
            return None

        if root in nodes:
            return root

        left = self._lca(root.left, nodes)
        right = self._lca(root.right, nodes)

        if left and right:
            return root

        return left if left else right
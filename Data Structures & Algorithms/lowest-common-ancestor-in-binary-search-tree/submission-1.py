# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self._dfs(root, p, q)

    def _dfs(
        self, node: TreeNode | None, 
        first: TreeNode, 
        second: TreeNode
    ) -> TreeNode | None:
        if not node:
            return None

        if node.val == first.val or node.val == second.val:
            return node

        left = self._dfs(node.left, first, second)
        right = self._dfs(node.right, first, second)

        if left and right:
            return node

        return left if left else right
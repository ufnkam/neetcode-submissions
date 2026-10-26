# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self._dfs(root, p, q)
    
    def _dfs(self, node: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
        if not node: return None
        if node.val == p.val or node.val == q.val:
            return node
        left = self._dfs(node.left, p, q)
        right = self._dfs(node.right, p, q)
        if left and right: 
            return node
        return left if left else right

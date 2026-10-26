# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self._dfs(p, q)

    def _dfs(self, node_p: TreeNode | None, node_q: TreeNode | None) -> bool:
        if not node_p and not node_q: return True
        if not node_p or not node_q: return False
        if node_p.val != node_q.val: 
            return False
        left_p = self._dfs(node_p.left, node_q.left)
        right_p = self._dfs(node_p.right, node_q.right)
        return left_p and right_p
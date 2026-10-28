# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.best = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self._dfs(root)
        return self.best

    def _dfs(self, node: TreeNode | None):
        if not node: return 0
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        self.best = max(self.best, left + right)
        return 1 + max(left, right)
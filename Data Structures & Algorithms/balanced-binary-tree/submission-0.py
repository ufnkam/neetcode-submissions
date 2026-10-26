# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.is_balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self._dfs(root)
        return self.is_balanced

    def _dfs(self, node: TreeNode | None) -> int:
        if not node: return 0
        left = self._dfs(node.left)
        right = self._dfs(node.right)
        if abs(left - right) > 1:
            self.is_balanced = False
        return 1 + max(left, right)

        
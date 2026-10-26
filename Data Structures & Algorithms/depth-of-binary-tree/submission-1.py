# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._dfs(root)

    def _dfs(
        self,
        node: TreeNode | None,
    ) -> None:
        if not node: return 0

        left = self._dfs(node.left)
        right = self._dfs(node.right)
        return 1 + max(left, right)




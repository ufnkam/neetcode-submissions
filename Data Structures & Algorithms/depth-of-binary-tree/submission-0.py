# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        deep = 0
        self._dfs(root, deep)
        return self.depth

    def _dfs(
        self,
        node: TreeNode | None,
        deep: int
    ) -> None:
        if not node: 
            return

        current = deep + 1
        self.depth = max(current, self.depth)

        self._dfs(node.left, current)
        self._dfs(node.right, current)

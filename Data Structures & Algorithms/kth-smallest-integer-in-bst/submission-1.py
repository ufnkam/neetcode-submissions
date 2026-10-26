# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.search = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.search = []
        self._dfs(root)
        return self.search[k-1]

    def _dfs(
        self,
        node: TreeNode | None,
    ) -> None:
       if not node: return 
       left = self._dfs(node.left)
       self.search.append(node.val)
       right = self._dfs(node.right) 

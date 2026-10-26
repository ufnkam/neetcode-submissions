# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.good_nodes = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        self._dfs(root, float('-inf'))
        return self.good_nodes

    def _dfs(self, node: TreeNode, path_max: int) -> None:
        if not node: return
        if node.val >= path_max:
            self.good_nodes += 1
        path_max = max(node.val, path_max)
        self._dfs(node.left, path_max)
        self._dfs(node.right, path_max)


        
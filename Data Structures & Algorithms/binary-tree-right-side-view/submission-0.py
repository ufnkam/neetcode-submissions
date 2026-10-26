# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            lsize = len(queue)
            rbound = lsize - 1
            for i in range(lsize):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i < rbound: continue
                result.append(node.val)
        return result       
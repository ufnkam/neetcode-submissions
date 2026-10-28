class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def __init__(self) -> None:
            self.parent = []

        n = len(edges)
        self.parent = list(range(n + 1))
        for src, dst in edges:
            if not self._union(src, dst):
                return [src, dst]
        return []

    def _find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    def _union(self, src: int, dst: int) -> bool:
        src_root, dst_root = self._find(src), self._find(dst)
        if src_root == dst_root:
            return False
        self.parent[dst_root] = src_root
        return True
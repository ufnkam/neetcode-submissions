class Solution:
    def __init__(self) -> None:
        self.parent = []

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                edges.append((weight, i, j))
        edges.sort()
        self.parent = list(range(n + 1))
        used = 0
        total = 0
        for weight, p1, p2 in edges:
            if not self._union(p1, p2): continue
            used += 1
            total += weight
        return total

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



        
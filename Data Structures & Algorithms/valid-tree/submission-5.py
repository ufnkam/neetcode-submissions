from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        graph = dict(graph)
        visited = set()
        is_cycle = self._detect_cycle(0, graph, visited, None)
        if len(visited) < n: return False
        return not is_cycle

    def _detect_cycle(
        self, 
        node: int, 
        graph: dict[int, list[int]], 
        visited: set[int],
        parent: int | None,
    ) -> bool:
        visited.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                if self._detect_cycle(n, graph, visited, node):
                    return True
            elif n != parent:
                return True
        return False



        

        
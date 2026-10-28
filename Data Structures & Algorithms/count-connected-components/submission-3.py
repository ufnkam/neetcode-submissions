from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        graph = dict(graph)
        visited = set()
        components = 0
        for node in range(n):
            if node not in visited:
                component = []
                self._dfs(node, graph, visited, component)
                components += 1
        return components

    def _dfs(
        self,
        node: int,
        graph: dict[int, list[int]],
        visited: set[int], 
        component: list[int],
    ) -> None:
        visited.add(node)
        component.append(node)
        for n in graph.get(node, []):
            if n not in visited:
                self._dfs(n, graph, visited, component)



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        graph = dict(graph)

        visited: set[int] = set()
        components = []

        for i in range(n):
            if i not in visited:
                component = []
                self._dfs(
                    graph, i, component, visited
                )
                components.append(component)

        return len(components)

    def _dfs(
        self,
        graph: dict[int, list[int]],
        node: int,
        component: list[int],
        visited: set[int],   
    ) -> None:
        visited.add(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                component.append(neighbour)
                self._dfs(
                    graph,
                    neighbour,
                    component,
                    visited
                )



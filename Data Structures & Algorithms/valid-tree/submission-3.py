from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        graph = dict(graph)

        if not graph:
            return n == 1

        visited: set[int] = set()

        if not self.is_tree(graph, 0, visited, None):
            return False

        return len(visited) == n


    def is_tree(
        self, 
        graph: dict[int, list[int]], 
        node: int, 
        visited: set[int], 
        parent: int | None,
    ) -> bool:
        visited.add(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                if not self.is_tree(
                    graph,
                    neighbour,
                    visited,
                    node
                ):
                    return False
            elif neighbour != parent:
                return False

        return True



        

        
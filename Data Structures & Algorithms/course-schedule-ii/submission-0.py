from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)
        graph = dict(graph)
        visited: set[int] = set()
        result: list[int] = []
        for node in range(numCourses):
            if node not in visited:
                if self._topo_sort(node, graph, visited, result, set()):
                    return []
        return result

    def _topo_sort(
        self, 
        node: int, 
        graph: list[list[int]], 
        visited: set[int], 
        result: list[int],
        path: set[int],
    ) -> bool:
        visited.add(node)
        path.add(node)
        for n in graph.get(node, []):
            if n not in visited:
                if self._topo_sort(n, graph, visited, result, path):
                    return True
            elif n in path:
                return True

        result.append(node)
        path.remove(node)
        return False


from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)
        graph = dict(graph)
        visited: set[int] = set()
        for node in range(numCourses):
            if node in visited: continue
            if self._has_cycles(node, graph, visited, set()): return False
        return True

    def _has_cycles(
        self, 
        node: int, 
        graph: dict[int, list[int]], 
        visited: set[int], 
        path: set[int]
    ) -> bool:
        visited.add(node)
        path.add(node)
        for n in graph.get(node, []):
            if n not in visited: 
                if self._has_cycles(n, graph, visited, path):
                    return True

            elif n in path:
                return True 

        path.remove(node)
        return False

        


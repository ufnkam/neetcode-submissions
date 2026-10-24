from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)

        graph = dict(graph)
        visited: set[int] = set()
        result: list[int] = []
        path: set[int] = set()
        
        for i in range(numCourses):
            if i not in visited:
                if self.dfs(
                    graph, i, visited, result, path
                ):
                    return False
        return True

    def dfs(self, graph: dict[int, list[int]], node: int, visited: set[int], result: list[int], path: set[int]) -> bool:
        visited.add(node)
        path.add(node)

        for neighbour in graph.get(node, []):
            if neighbour in path:
                return True

            if neighbour not in visited:
                if self.dfs(
                    graph, neighbour, visited, result, path
                ):
                    return True

        result.append(node)
        path.remove(node)
        return False



from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        for word in words:
            for c in word:
                graph[c] = []
        l, r = 0, 1
        while r < len(words):
            word1 = words[l]
            word2 = words[r]
            min_len = min(len(word1), len(word2))
            i = 0
            while i < min_len:
                if word1[i] != word2[i]: 
                    graph[word1[i]].append(word2[i])
                    break
                i += 1
            if i == min_len and len(word1) > len(word2):
                return ""
            l += 1
            r += 1
        graph = dict(graph)
        visited = set()
        result = []
        for node in graph:
            if node in visited: continue
            if self._dfs(node, graph, visited, result, set()): 
                return ""
        result.reverse()
        return "".join(result)
    
    def _dfs(
        self, 
        node: str, 
        graph: dict[str, list[str]], 
        visited: set[str], 
        result: list[str],
        path: set[str],
    ) -> bool:
        visited.add(node)
        path.add(node)
        for ne in graph[node]:
            if ne not in visited:
                if self._dfs(ne, graph, visited, result, path):
                    return True
            elif ne in path:
                return True

        result.append(node)
        path.remove(node)
        return False


        
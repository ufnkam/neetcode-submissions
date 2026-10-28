import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 0: return 0
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        dist = [float('inf')] * (n + 1)
        pq = []
        dist[k] = 0
        heapq.heappush(pq, (0, k))
        while pq:
            _, node = heapq.heappop(pq)
            for ne, weight in graph.get(node, []):
                if (
                    dist[node] != float('inf')
                    and dist[node] + weight < dist[ne]
                ):
                    dist[ne] = dist[node] + weight
                    heapq.heappush(pq, (dist[ne], ne))
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1

        return max(dist[1:])


from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(
        self, 
        n: int, 
        flights: List[List[int]], 
        src: int, 
        dst: int, 
        k: int
    ) -> int:
        if n == 0: return -1
        graph = defaultdict(list)
        for _src, _dst, cost in flights:
            graph[_src].append((_dst, cost))
        min_stops = [float('inf')] * n
        pq = []
        # price, node, stops
        heapq.heappush(pq, (0, src, 0))
        while pq:
            node_cost, node, stops = heapq.heappop(pq)
            if node == dst: return node_cost
            if stops >= k + 1 or stops > min_stops[node]: continue
            min_stops[node] = stops
            for ne, weight in graph.get(node, []):
                heapq.heappush(pq, ((node_cost + weight, ne, stops + 1)))

        return -1



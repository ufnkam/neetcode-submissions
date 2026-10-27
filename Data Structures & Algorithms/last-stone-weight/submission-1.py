import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 == stone2: continue
            else: 
                new = abs(stone1 - stone2)
                heapq.heappush(heap, -new)

        return -heap[0] if heap else 0
                        
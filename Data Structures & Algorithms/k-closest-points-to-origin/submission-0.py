import heapq
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [
            (-sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2), point)
            for point in points
        ]
        heapq.heapify(distances)
        while len(distances) > k: heapq.heappop(distances)
        return [point[1] for point in distances]
        
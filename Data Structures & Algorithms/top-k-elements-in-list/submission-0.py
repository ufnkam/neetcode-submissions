from heapq import heapify_max, heappop_max

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict(Counter(nums))

        if k > len(counter):
            k = len(counter)

        heap = [(v, k) for k, v in counter.items()]
        heapify_max(heap)

        highest = []
        for _ in range(k):
            val = heappop_max(heap)
            highest.append(val[1])

        return highest
    
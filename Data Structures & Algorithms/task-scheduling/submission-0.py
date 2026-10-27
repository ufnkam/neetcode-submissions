import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        cooldown = deque([])
        timer = 0
        while heap or cooldown:
            if heap:
                count, task = heapq.heappop(heap)
                count += 1
                if count < 0:
                    cooldown.append((timer, count, task))
            if cooldown and timer - cooldown[0][0] >= n:
                _, count, task = cooldown.popleft()
                heapq.heappush(heap, (count, task))
            timer += 1

        return timer

        
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        result = []
        n = len(nums)
        start = 0
        heap = [(-val, i) for i, val in enumerate(nums) if i < k - 1]
        heapq.heapify(heap)
        for end in range(k - 1, n):
            heapq.heappush(heap, (-nums[end], end))
            while heap[0][1] < start:
                heapq.heappop(heap)
            result.append(-heap[0][0])
            start += 1

        return result
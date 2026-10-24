class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pairs = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        return [i[0] for i in pairs]


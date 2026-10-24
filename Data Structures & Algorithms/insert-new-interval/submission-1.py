class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged:
                merged.append(interval)
                continue

            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)
            
        return merged
        
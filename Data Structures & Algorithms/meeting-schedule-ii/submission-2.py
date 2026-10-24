"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start >= ends[end_ptr]:
                end_ptr += 1
            else:
                rooms += 1
        
        return rooms
            

        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort intervals based on their start times
        intervals.sort(key=lambda interval: interval.start)
        # Heap keeps track of the earliest end time
        min_heap = []

        for interval in intervals:
            # Heap is not empty (room is occupied) and the smallest end time is lower than the current meeting's start time -> room reuse
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            # Occupy a different room
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

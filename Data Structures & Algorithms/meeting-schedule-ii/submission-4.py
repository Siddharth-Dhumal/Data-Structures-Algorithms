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
        intervals_list = []

        for i in intervals:
            intervals_list.append([i.start, i.end])

        intervals_list.sort()

        rooms = []
        heapq.heapify(rooms)
        heapq.heappush(rooms, intervals_list[0][-1])

        for i in range(1, len(intervals_list)):
            if intervals_list[i][0] < rooms[0]:
                heapq.heappush(rooms, intervals_list[i][-1])
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, intervals_list[i][-1])
        
        return len(rooms)
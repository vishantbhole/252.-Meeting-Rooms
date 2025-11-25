# 252. Meeting Rooms
#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

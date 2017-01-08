class Solution(object):
    def insert(self, intervals, newInterval):
        a, n = 0, len(intervals)
        t = newInterval
        while a < n and intervals[a].end < t.start:
            a += 1
        if a < n:
            t.start = min(t.start, intervals[a].start)
        b = a
        while b < n and intervals[b].start <= t.end:
            t.end = max(t.end, intervals[b].end)
            b += 1
        return intervals[:a] + [t] + intervals[b:]

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)
        r = []
        m = -(1 << 31)
        for x in intervals:
            if x.start <= m:
                if x.end > m:
                    m = last.end = x.end
            else:
                r.append(x)
                last = r[-1]
                m = last.end
        return r

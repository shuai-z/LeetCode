class Solution(object):
    def groupAnagrams(self, strs):
        r, m = [], {}
        for s in strs:
            l = list(s)
            l.sort()
            t = ''.join(l)
            idx = m.get(t, -1)
            if idx >= 0:
                r[idx].append(s)
            else:
                m[t] = len(r)
                r.append([s])
        return r

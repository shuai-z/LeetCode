class Solution(object):
    def combinationSum(self, candidates, target):
        r, l = [], []
        i, cl = 0, len(candidates)
        candidates.sort()
        while i < cl:
            x = candidates[i]
            while target >= x:
                l.append(i)
                target -= x
            if target == 0:
                r.append([candidates[i] for i in l])
                target += candidates[l.pop()]
            if not l:
                break
            i = l.pop() + 1
            target += candidates[i-1]
            while i >= cl and l:
                i = l.pop() + 1
                target += candidates[i-1]
        return r

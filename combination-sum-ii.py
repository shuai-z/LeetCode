class Solution(object):
    def combinationSum2(self, candidates, target):
        r, l = [], []
        i, cl = 0, len(candidates)
        candidates.sort()
        while i < cl:
            x = candidates[i]
            while target >= x:
                l.append(i)
                target -= x
                i += 1
                if i >= cl: break
                x = candidates[i]
            if target == 0:
                r.append([candidates[k] for k in l])
                target += candidates[l.pop()]
            if not l:
                break
            i = l.pop() + 1
            target += candidates[i-1]
            while True:
                while i < cl and candidates[i] == candidates[i-1]:
                    i += 1
                if i >= cl and l:
                    i = l.pop() + 1
                    target += candidates[i-1]
                else:
                    break
        return r

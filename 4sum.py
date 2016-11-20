class Solution(object):
    def fourSum(self, nums, target):
        nn, t = len(nums), target >> 1
        m, r = {}, set()
        nums.sort()
        for i in range(nn):
            for j in range(i+1, nn):
                s = nums[i] + nums[j]
                if s in m:
                    m[s].append((i, j))
                else:
                    m[s] = [(i, j)]
        for a in m.keys():
            if a > t: continue
            b = target - a
            if b in m:
                va, vb = m[a], m[b]
                for x in va:
                    for y in vb:
                        if y[0] > x[1]:
                            r.add((nums[x[0]], nums[x[1]], nums[y[0]], nums[y[1]]))
        return [list(x) for x in r]

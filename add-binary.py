class Solution(object):
    def addBinary(self, a, b):
        m = {'0':0, '1':1}
        r, ov = '', 0
        ia, ib = len(a)-1, len(b)-1
        while ia >= 0 or ib >= 0 or ov:
            xa = xb = 0
            if ia >= 0:
                xa = m[a[ia]]
                ia -= 1
            if ib >= 0:
                xb = m[b[ib]]
                ib -= 1
            t = xa + xb + ov
            if t >= 2:
                ov, t = 1, t-2
            else:
                ov = 0
            r = str(t) + r
        return r

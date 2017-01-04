class Solution(object):
    def myPow(self, x, n):
        i, r, f = 1, 1, False
        if n < 0:
            n, f = -n, True
        while i <= n:
            t = x
            while i*2 <= n:
                t *= t
                i *= 2
            n -= i
            i = 1
            r *= t
        if f: return 1.0/f
        return f

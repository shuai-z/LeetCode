class Solution:
    def convert(self, s, n):
        l, m = len(s), n + (n-2) or 1
        r = []
        for k in range(0, l, m):
            r.append(s[k])
        for i in range(1, n-1):
            for k in range(i, l, m):
                r.append(s[k])
                k += m-2*i
                if k < l:
                    r.append(s[k])
        if n > 1:
            for k in range(n-1, l, m):
                r.append(s[k])
        return ''.join(r)

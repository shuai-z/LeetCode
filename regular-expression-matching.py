# 虽然这类题一般都用DFA/NFA来做，但还是想换个角度试一下（还可以优化）.
class Solution(object):
    def isMatch(self, s, p):
        x, plen = set([0]), len(p)
        for c in s:
            v = set()
            for i in x:
                if i >= plen: continue
                if i < plen-1 and p[i+1] == '*':
                    i += 1

                if p[i] == '*':
                    while i < plen and p[i] == '*':
                        # catch syntax error
                        if i == 0 or p[i-1] == '*': return False
                        if p[i-1] == c or p[i-1] == '.':
                            v.add(i)
                        i += 2
                    i -= 1
                if i < plen and (p[i] == c or p[i] == '.'):
                    v.add(i+1)
            if len(v) == 0: return False
            x = v
        m = len(x) > 0 and max(x)
        if m < plen:
            if m < plen-1 and p[m+1] == '*':
                m += 1
            while m < plen and p[m] == '*':
                if m == 0 or p[m-1] == '*': return False
                m += 2
            m -= 1
        return m == plen

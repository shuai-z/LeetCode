class Solution(object):
    def romanToInt(self, s):
        v = {'*':0,'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        n, x = 0, '*'
        for c in s:
            if v[x] < v[c]:
                n -= v[x] * 2
            n += v[c]
            x = c
        return n

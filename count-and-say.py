def Solution(object):
    def countAndSay(self, n):
        s, r = '1', ''
        while n > 1:
            n -= 1
            lastc, m = s[0], 0
            for c in s:
                if c == lastc:
                    m += 1
                else:
                    r += str(m) + lastc
                    lastc, m = c, 1
            else:
                r += str(m) + lastc
            s, r = r, ''
        return s

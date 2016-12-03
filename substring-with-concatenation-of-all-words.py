class Solution(object):
    def findSubstring(self, s, words):
        r, m = [], {}
        slen, ws, n = len(s), len(words), len(words[0])
        # ...
        if n == 0:
            return range(slen+1)
        for w in words:
            m[w] = m.get(w, 0) + 1
        for d in range(n):
            i = j = d
            while j <= slen:
                while m.get(s[j:j+n]) > 0:
                    m[s[j:j+n]] -= 1
                    ws -= 1
                    j += n
                if ws == 0:
                    r.append(i)
                while s[i:i+n] != s[j:j+n]:
                    m[s[i:i+n]] += 1
                    ws += 1
                    i += n
                i, j = i+n, j+n
        return r

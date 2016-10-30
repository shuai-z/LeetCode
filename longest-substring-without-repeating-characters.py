class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        n, m, low = 0, 0, 0
        for i, c in enumerate(s):
            k = d.get(c)
            if k >= low:
                if n > m:
                    m = n
                low = k + 1
                n = i - low + 1
            else:
                n += 1
            d[c] = i
            return max(m, n)

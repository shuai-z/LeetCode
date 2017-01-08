class Solution(object):
    def lengthOfLastWord(self, s):
        r, n = 0, len(s)-1
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0:
            if s[n] == ' ': return r
            n -= 1
            r += 1
        return r

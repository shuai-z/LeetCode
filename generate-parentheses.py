class Solution(object):
    def generateParentheses(self, n):
        self.r = []
        self.gen('', n, n)
        return self.r

    def gen(self, s, nl, nr):
        if nr == 0:
            self.r.append(s)
            return
        if nl > 0:
            self.gen(s+'(', nl-1, nr)
        if nr > nl:
            self.gen(s+')', nl, nr-1)

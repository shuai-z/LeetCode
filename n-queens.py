class Solution(object):
    def solveNQueens(self, n):
        self.n = n
        self.r = []
        self.li = [-1 for _ in range(n)]
        t = [-1 for _ in range(2*n)]
        self.la, self.lb = t[:], t[:]
        self.recur(0)
        return self.r

    def recur(self, cur):
        if cur == self.n:
            b = []
            for i, idx in enumerate(self.li):
                b.append('.'*idx + 'Q' + '.'*(self.n-idx-1))
            self.r.append(b)
            return
        for i in range(self.n):
            a, b = cur+i, cur-i
            if self.la[a] == -1 and self.lb[b] == -1 and self.li[i] == -1:
                self.la[a] = self.lb[b] = self.li[i] = cur
                self.recur(cur+1)
                self.la[a] = self.lb[b] = self.li[i] = -1

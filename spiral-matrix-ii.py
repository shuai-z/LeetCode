class Solution(object):
    def generateMatrix(self, n):
        v = [0 for _ in range(n)]
        r = [v[:] for _ in range(n)]
        k = i = 0
        while k < n*n:
            for y in range(i, n-1):
                r[i][y] = k = k+1
            for x in range(i+1, n-i):
                r[x][n-i-1] = k = k+1
            for y in range(n-i-2, i-1, -1):
                r[n-i-1][y] = k = k+1
            for x in range(n-i-2, i, -1):
                r[x][i] = k = k+1
            i += 1
        return r

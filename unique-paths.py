class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        r = [1 for _ in range(n)]
        r = [r[:] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = r[i-1][j] + r[i][j-1]
        return r[m-1][n-1]

class Solution(object):
    def minPathSum(self, g):
        if not g or not g[0]:
            return 0
        m, n = len(g), len(g[0])
        x = g[0][0]
        for j in range(1, n):
            x = g[0][j] = x + g[0][j]
        x = g[0][0]
        for i in range(1, m):
            x = g[i][0] = x + g[i][0]
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] = min(g[i-1][j], g[i][j-1]) + g[i][j]
        return g[m-1][n-1]

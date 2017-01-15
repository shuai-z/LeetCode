class Solution(object):
    def uniquePathsWithObstacles(self, g):
        if not g or g[0][0] == 1:
            return 0
        m, n = len(g), len(g[0])
        v = 1
        for j in range(n):
            if g[0][j] == 1:
                v = 0
            g[0][j] = v
        for i in range(1, m):
            for j in range(n):
                if g[i][j] == 1:
                    g[i][j] = 0
                else:
                    g[i][j] = (g[i][j-1] if j > 0 else 0) + g[i-1][j]
        return g[m-1][n-1]

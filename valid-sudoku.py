class Solution(object):
    def isValidSudoku(self, board):
        s = [[], [], []]
        for x in range(3):
            s[x] = [[] for _ in range(9)]
            for i in range(9):
                s[x][i] = [False for _ in range(10)]
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == '.': continue
                ci = int(c)
                b = 3 * (i/3) + j/3
                if s[0][i][ci] or s[1][j][ci] or s[2][b][ci]:
                    return False
                s[0][i][ci] = s[1][j][ci] = s[2][b][ci] = True
        return True

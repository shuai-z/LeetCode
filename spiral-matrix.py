class Solution(object):
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix and matrix[0])
        r, i = [], 0
        while True:
            if i >= cols-i: break
            for y in range(i, cols-i):
                r.append(matrix[i][y])
            if i >= rows-i-1: break
            for x in range(i+1, rows-i):
                r.append(matrix[x][cols-i-1])
            if i >= cols-i-1: break
            for y in range(cols-i-2, i-1, -1):
                r.append(matrix[rows-i-1][y])
            if i >= rows-i-2: break
            for x in range(rows-i-2, i, -1):
                r.append(matrix[x][i])
            i += 1
        return r

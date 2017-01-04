class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n/2):
            matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]

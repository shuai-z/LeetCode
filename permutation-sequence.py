class Solution(object):
    def getPermutation(self, n, k):
        np = [1]
        for i in range(1, n):
            np.append(np[i-1] * i)
        r = ''
        v = range(1, n+1)
        k -= 1
        for i in range(n):
            x, k = divmod(k, np[n-1-i])
            r += str(v[x])
            v = v[:x] + v[x+1:]
        return r

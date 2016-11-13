class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        k, n = x % 10, 0
        while x > n:
            n = n*10 + x%10
            x /= 10
        return x == n or (k != 0 and x == n/10)

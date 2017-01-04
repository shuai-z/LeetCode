class Solution(object):
    def canJump(self, nums):
        j, mx = 0, 0
        for i, n in enumerate(nums[:-1]):
            j = max(i+n, j)
            if i == mx:
                if j == mx: return False
                mx = j
        return True

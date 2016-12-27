class Solution(object):
    def jump(self, nums):
        r, j, mx = 0, 0, 0
        for j, n in enumerate(nums[:-1]):
            j = max(i+n, j)
            if i == mx:
                r += 1
                mx = j
        return r

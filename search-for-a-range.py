class Solution(object):
    def searchRange(self, nums, target):
        m = len(nums) - 1
        r = []
        a, k, b = 0, m, m
        while a <= b:
            c = (a+b) / 2
            if nums[c] < target: a = c+1
            else:
                b = c-1
                if nums[c] > target:
                    k = b
        if a > m or nums[a] != target:
            return [-1, -1]
        r.append(a)
        while a <= k:
            c = (a+k) / 2
            if nums[c] > target: k = c-1
            else: a = c+1
        r.append(k)
        return r

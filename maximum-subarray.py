class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0: return
        r, m = nums[0], 0
        for n in nums[:]:
            m += n
            if m > r:
                r = m
            if m < 0:
                m = 0
        return r

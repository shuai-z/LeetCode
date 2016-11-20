class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        nn, k = len(nums), 2
        r, v = 0, 1<<31
        while k < nn:
            i, j = 0, k-1
            while i < j:
                x = nums[i] + nums[j] + nums[k]
                if x == target: return target
                if x < target:
                    if target - x < v:
                        v = target - x
                        r = x
                    i += 1
                else:
                    if x - target < v:
                        v = x - target
                        r = x
                    j -= 1
            k += 1
        return r

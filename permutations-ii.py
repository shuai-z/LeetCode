class Solution(object):
    def permute(self, nums):
        self.r = []
        self.perm(nums, 0)
        return self.r

    def perm(self, nums, i):
        if i == len(nums)-1:
            self.r.append(nums[:])
        s = set()
        for k in range(i, len(nums)):
            if nums[k] in s: continue
            s.add(nums[k])
            nums[i], nums[k] = nums[k], nums[i]
            self.perm(nums, i+1)
            nums[i], nums[k] = nums[k], nums[i]

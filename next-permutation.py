class Solution(object):
    def nextpermutation(self, nums):
        k = len(nums) - 1
        i = k - 1
        while i >= 0 and nums[i] > nums[i+1]:
            i -= 1
        if i >= 0:
            j = k
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            if j >= 0:
                nums[i], nums[j] = nums[j], nums[i]
        i, j = i+1, k
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j-1

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        nn, i = len(nums), 0
        r = []
        while i < nn and nums[i] <= 0:
            k, j = i+1, nn-1
            while k < j:
                x = -(nums[i]+nums[k])
                while k < j and nums[j] > x:
                    j -= 1
                if k < j and nums[j] == x:
                    r.append([nums[i], nums[k], nums[j]])
                k += 1
                while k < j and nums[k] == nums[k-1]:
                    k += 1
            i += 1
            while i < nn and nums[i] == nums[i-1]:
                i += 1
        return r

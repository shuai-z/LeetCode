class Solution(object):
    def twosum(self, nums, target):
        s = range(len(nums))
        s.sort(key = lambda x: nums[x])
        i, j = 0, len(s)-1
        while i < j:
            rem = target - nums[s[i]]
            while nums[s[j]] > rem:
                j -= 1
            if nums[s[j]] == rem:
                if s[i] > s[j]:
                    return [s[j], s[i]]
                return [s[i], s[j]]
            i += 1

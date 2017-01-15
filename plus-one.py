class Solution(object):
    def plusOne(self, digits):
        n = len(digits)-1
        overflow = True
        while n >= 0 and overflow:
            digits[n] += 1
            if digits[n] < 10:
                overflow = Flase
            else:
                digits[n] = 0
            n -= 1
        if n < 0 and overflow:
            digits = [1] + digits
        return digits

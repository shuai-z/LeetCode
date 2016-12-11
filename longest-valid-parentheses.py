class Solution(object):
    def longestValidParentheses(self, s):
        stk, r = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif len(stk) > 1:
                stk.pop()
                x = i - stk[-1]
                if x > r: r = x
            else:
                stk[0] = i
        return r

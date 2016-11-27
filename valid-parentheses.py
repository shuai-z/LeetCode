class Solution(object):
    def isValid(self, s):
        pair = {'(':')', '[':']', '{':'}'}
        a = []
        for c in s:
            if c in '([{':
                a.append(pair[c])
            else:
                if len(a) == 0 or a[-1] != c:
                    return False
                a.pop()
        return len(a) == 0

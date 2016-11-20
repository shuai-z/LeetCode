class Solution(object):
    def letterCombinations(self, digits):
        a = [' ','*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        r, t = [], ['']
        for c in digits:
            i = int(c)
            r = []
            for p in t:
                for x in a[i]:
                    r.append(p+x)
            t = r
        return r

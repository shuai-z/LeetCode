class Solution(object):
    def strStr(self, haystack, needle):
        hl, nl = len(haystack), len(needle)
        i = nl-1
        while i < hl:
            j, k = nl-1, i
            while j >= 0:
                if needle[j] != haystack[k]:
                    break
                j, k = j-1, k-1
            else:
                return k+1
            i, j = i+1, j-1
            while j >= 0:
                if haystack[k] == needle[j]:
                    break
                i, j = i+1, j-1
        return -1

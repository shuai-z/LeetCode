# lazy...
class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False

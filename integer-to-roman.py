class Solution(object):
    def intToRoman(self, num):
        m = [
            [1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],
            [100,'C'],[90,'XC'],[50,'L'],[40,'XL'],
            [10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']
        ]
        s = ''
        for x in m:
            while num >= x[0]:
                s += x[1]
                num -= x[0]
        return s

    def intToRoman2(self, num):
        """
        num: 1~3999
        """
        v = ['I','','V','X','','L','C','','D','M','','*','*']
        i, s = 0, ''
        while num > 0:
            j = i + 1
            num, r = divmod(num, 10)
            if r >= 5:
                j += 1
                r -= 5
            if r == 4:
                s = v[i] + v[j+1] + s
            else:
                s = v[j] + v[i]*r + s
            i += 3
        return s

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x = l = ListNode(0)
        f = 0
        while l1 or l2 or f:
            if l1:
                f += l1.val
                l1 = l1.next
            if l2:
                f += l2.val
                l2 = l2.next
            x.next = listNode(f % 10)
            x = x.next
            f = f >= 10 and 1 or 0
        return l.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        r = c = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                c.next = l1
                l1 = l1.next
            else:
                c.next = l2
                l2 = l2.next
            c = c.next
        c.next = l1 or l2
        return r.next

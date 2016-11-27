# use heapq (added __lt__ to ListNode)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        ListNode.__lt__ = (lambda self, b: self.val < b.val)
        h = []
        p = r = ListNode(0)
        for it in lists:
            if it: h.append(it)
        heapq.heapify(h)
        n = len(h)
        while n > 0:
            a = heapq.heappop(h)
            p.next = a
            p = p.next
            if not a.next: n -= 1
            else: heapq.heappush(h, a.next)
        return r.next

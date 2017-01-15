class Solution(object):
    def rotateRight(self, head, k):
        if not head: return head
        n = 0
        p = q = head
        while k > 0:
            q = q.next
            n += 1
            k -= 1
            if not q:
                # over
                q = p
                k %= n
        if p == q: return head
        while q.next:
            p, q = p.next, q.next
        tmp, p.next = p.next, q.next
        if head != q: # avoid circle
            q.next = head
        return tmp

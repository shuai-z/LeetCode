struct ListNode* reverseKGroup(sruct ListNode* head, int k) {
  struct ListNode t = {0, head}, *p, *q, *x, *y;
  int i;
  if (k <= 1) return head;

  p = &t;
  while ((q = p)) {
    for (i = 0; i < k; i++) {
      q = q->next;
      if (!q) return t.next;
    }
    x = p->next;
    p->next = q;
    p = x;
    while (x != q) {
      y = x->next;
      x->next = q->next;
      q->next = x;
      x = y
    }
  }
  return t.next;
}

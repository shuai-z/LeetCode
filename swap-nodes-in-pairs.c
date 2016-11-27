struct ListNode* swapPairs(struct ListNode* head) {
  struct ListNode t = {0, head}, *p, *q;
  p = &t;
  while (p->next && (q = p->next->next)) {
    p->next->next = q->next;
    q->next = p->next;
    p->next = q;
    p = q->next;
  }
  return t.next;
}

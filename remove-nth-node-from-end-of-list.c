struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
  struct ListNode x={0, head}, *p, *q;
  p = q = &x;
  while (n--) p = p->next;
  while ((p = p->next)) q = q->next;
  q->next = q->next->next;
  return x.next;
}

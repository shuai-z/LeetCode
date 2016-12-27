int trap(int* height, int heightSize) {
  int *p = height, *q = height+heightSize-1, r = 0, m;
  while (p < q) {
    m = *p < *q ? *p++ : *q--;
    while (p <= q && *p <= m) {
      r += (m - *p++);
    }
    while (p <= q && *q <= m) {
      r += (m - *q--);
    }
  }
  return r;
}

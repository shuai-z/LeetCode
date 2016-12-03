int divide(int dividend, int divisor) {
  long long a = llabs(dividend), b = llabs(divisor), c, r = 0, i = 1;
  if (b == 0) return INT_MAX;
  c = b;
  while (a >= (c << 1)) {
    c <<= 1;
    i <<= 1;
  }
  while (a >= b) {
    while (a < c) {
      c >>= 1;
      i >>= 1;
    }
    a -= c;
    r += i;
  }
  if ((dividend ^ divisor) >> 31) r = -r;
  if (r < INT_MIN) r = INT_MIN;
  else if (r > INT_MAX) r = INT_MAX;
  return r;
}

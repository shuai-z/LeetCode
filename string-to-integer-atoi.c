int myAtoi(char* p) {
  int n=0, f=1, k, X=INT_MAX/10;
  while (isspace(*p)) p++;
  if (*p == '-') {
    f = -1;
    p++;
  } else if (*p == '+') {
    p++;
  }
  while(isdigit(*p)) {
    k = (*p++) - '0';
    if (n > X || (n == X && k > 7)) return INT_MAX;
    if (n < -X || (n == -X && k > 8)) return INT_MIN;
    n = n*10 + k*f;
  }
  return n;
}

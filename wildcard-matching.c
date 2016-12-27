// 本来直接改之前类似题的代码，发现这个更快，因为不需要那么多次循环
bool isMatch(char* s, char* p) {
  char *star = NULL, *ss = s;
  while (*s) {
    if (*p == '?' || *p == *s) {
      p++; s++;
    } else if (*p == '*') {
      star = p++; ss = s;
    } else if (star) {
      p = star+1; s = ++s;
    } else {
      return false;
    }
  }
  while (*p == '*') p++;
  return !*p;
}

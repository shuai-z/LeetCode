// This is slower than Manacher's algorithm.
//#include <stdlib.h>
//#include <string.h>

char* longestPalindrome(char* s) {
  int m=1, n=0, i=0, j, k, q, l[1000], lenp=strlen(s)+1;
  char c, *r = malloc(1000), *rs = s;
  while ((c = s[i++])) {
    for (j = k = 0; j < n && j <= lenp-i; j++) {
      q = l[j]+2;
      if (i-q >= 0 && c == s[i-q]) {
        l[k++] = q;
      }
    }
    l[k++] = 1;
    l[k++] = 0;
    n = k;
    if (l[0] > m) {
      m = l[0];
      rs = s + (i-m);
    }
  }
  strncpy(r, rs, m);
  r[m] = '\0';
  return r;
}

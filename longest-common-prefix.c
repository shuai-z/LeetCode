char* longestCommonPrefix(char** strs, int strsSize) {
  int n = 0, i;
  char *s = strsSize > 0 ? strs[0] : "", c;
  while ((c = *s++)) {
    for (i = 1; i < strsSize; i++) {
      if (strs[i][n] != c) {
        return strndup(strs[0], n);
      }
    }
    n++;
  }
  return strndup(strs[0], n);
}

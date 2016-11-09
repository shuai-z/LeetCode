// 提交之后看到大部分都是6ms才决定重新写的 - -
// 之前用的另一个比较直接的方法，～13ms:
//   ...
//   tmp = r*10 + x%10;
//   if (tmp/10 != r) return 0;
//   ...
int reverse(int x) {
  int r = 0, k, i = 0, b = x > 1000000000 || x < -1000000000 ? 1 : 0;
  int a[10] = {2,1,4,7,4,8,3,6,4,8};

  while (x) {
    k = x%10;
    if (b) {
      if (k > a[i] || k < -a[i]) return 0;
      if (k != a[i] && k != -a[i]) b = 0;
      else i++;
    }
    r = r*10 + k;
    x /= 10;
  }
  return r;
}

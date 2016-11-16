int maxArea(int* height, int heightSize) {
  int i=0, j=heightSize-1, m=0, k, c;
  do {
    k = height[i] < height[j] ? height[i++] : height[j--];
    c = (j-i+1) * k;
    if (c > m) {
      m = c;
    }
    while (height[i] <= k) i++;
    while (height[j] <= k) j--;
  } while (i < j);
  return m;
}

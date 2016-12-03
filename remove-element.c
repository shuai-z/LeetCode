int removeElement(int* nums, int numsSize, int val) {
  int *p=nums, *q=nums+(numsSize-1);
  while (p < q) {
    while (p < q && *p != val) p++;
    while (p < q && *q == val) q--;
    if (p < q) *p = *q--;
  }
  return (p - nums) + (numsSize == 0 || *p == val ? 0 : 1);
}

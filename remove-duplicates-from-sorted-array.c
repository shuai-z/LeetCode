int removeDuplicates(int* nums, int numsSize) {
  int r = 0, i, x, y;
  if (numsSize == 0) return 0;
  for (i = 1, y = nums[r++]; i < numsSize; i++) {
    if ((x = nums[i]) != y) {
      y = nums[r++] = x;
    }
  }
  return r;
}

int searchInsert(int* nums, int numsSize, int target) {
  int a = 0, b = numsSize-1, c;
  while (a <= b) {
    c = (a+b) / 2;
    if (nums[c] < target) a = c+1;
    else b = c-1;
  }
  return a;
}

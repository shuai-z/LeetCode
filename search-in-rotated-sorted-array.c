int search(int* nums, int numsSize, int target) {
  int a = 0, b = numsSize-1, c;
  while (a <= b) {
    c = (a+b) / 2;
    if (target == nums[c]) return c;
    if (target < nums[c]) {
      if (nums[a] < nums[b]) {
        if (target < nums[a]) return -1;
        else b = c-1;
      } else {
        if (nums[c] < nums[a] || target > nums[b]) b = c-1;
        else a = c+1;
      }
    } else {
      if (nums[a] < nums[b]) {
        if (target < nums[b]) return -1;
        else a = c+1;
      } else {
        if (nums[c] > nums[b] || target < nums[a]) a = c+1;
        else b = c-1;
      }
    }
  }
  return -1;
}

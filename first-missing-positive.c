// 一开始都没想到还可以改nums数组...所以感觉不可能用常量空间（这段代码是搜的别人的）
int firstMissingPositive(int* nums, int numsSize) {
  int i = 0, x;
  while (i < numsSize) {
    x = nums[i];
    if (x > 0 && x < numsSize && nums[x-1] != x) {
      nums[i] = nums[x-1];
      nums[x-1] = x;
    } else {
      i++;
    }
  }
  for (i = 0; i < numsSize; i++) {
    if (nums[i] != i+1)
      break;
  }
  return i+1;
}

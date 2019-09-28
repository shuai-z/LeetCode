/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
  return build(nums, 0, nums.length-1);
};

function build(nums, a, b) {
  if (a > b) return null;
  var k = ~~((a + b) / 2);
  var node = new TreeNode(nums[k]);
  node.left = build(nums, a, k-1);
  node.right = build(nums, k+1, b);
  return node;
}

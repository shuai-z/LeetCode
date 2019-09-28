/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
  var nums = toArray(head);
  return build(nums, 0, nums.length-1);
};

function toArray(head) {
  var r = [];
  while (head) {
    r.push(head.val);
    head = head.next;
  }
  return r;
}

function build(nums, a, b) {
  if (a > b) return null;
  var k = ~~((a + b) / 2);
  var node = new TreeNode(nums[k]);
  node.left = build(nums, a, k-1);
  node.right = build(nums, k+1, b);
  return node;
}

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
  let r = [];
  tr(root, r, 0);
  return r;
};


function tr(root, a, i) {
  if (!root) return;
  if (a.length <= i) a.push([]);
  if (i&1) {
    a[i].unshift(root.val);
  } else {
    a[i].push(root.val);
  }
  tr(root.left, a, i+1);
  tr(root.right, a, i+1);
}

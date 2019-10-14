/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
  if (!root) return [];
  sum -= root.val;
  if (!root.left && !root.right && sum === 0) return [[root.val]];
  var r = [
    pathSum(root.left, sum),
    pathSum(root.right, sum)
  ].filter(function (x) {
    return x.length > 0;
  });
  r = Array.prototype.concat.apply([], r);

  return r.map(function (x) {
    return [root.val].concat(x);
  });
};

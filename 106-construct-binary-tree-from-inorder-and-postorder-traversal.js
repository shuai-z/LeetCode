/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
  var root = new TreeNode();
  var t = [root];
  var node, tmp;
  var i, j;
  i = j = postorder.length - 1;
  while (i !== -1) {
    if (inorder[j] !== t[0].val) {
      node = new TreeNode(postorder[i]);
      t[0].right = node;
      t.unshift(node);
      i--;
    } else {
      while (inorder[j] === t[0].val) {
        tmp = t.shift();
        j--;
      }

      node = new TreeNode(postorder[i]);
      tmp.left = node;
      t.unshift(node);
      i--;
    }
  }
  return root.right;
};

// 105

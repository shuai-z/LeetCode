/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
  var root = new TreeNode();
  var t = [root];
  var node, tmp;
  var i, j;
  i = j = 0;
  while (i < preorder.length) {
    if (inorder[j] !== t[0].val) {
      node = new TreeNode(preorder[i]);
      t[0].left = node;
      t.unshift(node);
      i++;
    } else {
      while (inorder[j] === t[0].val) {
        tmp = t.shift();
        j++;
      }

      node = new TreeNode(preorder[i]);
      tmp.right = node;
      t.unshift(node);
      i++;
    }
  }
  return root.left;
};

// 只是觉得只遍历一次preorder和inorder是可以解出来的，暂时也没想到不需要额外空间或时间的递归方法。

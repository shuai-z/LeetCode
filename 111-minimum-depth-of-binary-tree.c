/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int minDepth(struct TreeNode* root){
  int a, b;
  if (!root) return 0;
  a = minDepth(root->left);
  b = minDepth(root->right);
  if (a == 0 || b == 0) return (a | b) + 1;
  return (a < b ? a : b) + 1;
}

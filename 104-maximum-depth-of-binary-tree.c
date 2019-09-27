/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int maxDepth(struct TreeNode* root){
  int a, b;
  if (!root) return 0;
  a = maxDepth(root->left);
  b = maxDepth(root->right);
  return (a > b ? a : b) + 1;
}


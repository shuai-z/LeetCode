/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int h(struct TreeNode* root) {
  int a, b;
  if (!root) return 0;
  a = h(root->left);
  if (a < 0) return -1;
  b = h(root->right);
  if (b < 0) return -1;
  if (abs(a - b) > 1) return -1;
  return (a > b ? a : b) + 1;
}

bool isBalanced(struct TreeNode* root){
  return h(root) >= 0;
}


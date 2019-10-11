/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool hasPathSum(struct TreeNode* root, int sum){
  if (!root) return false;
  sum -= root->val;
  return (!root->left && !root->right && sum == 0) ||
    hasPathSum(root->left, sum) ||
    hasPathSum(root->right, sum);
}

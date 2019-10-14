/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* f(struct TreeNode* root) {
  struct TreeNode* node;
  if (root->left) {
    node = f(root->left);
    node->right = root->right;
    root->right = root->left;
    root->left = NULL;
  } else {
    node = root;
  }
  while (node->right) {
    node = node->right;
  }
  return node;
}

void flatten(struct TreeNode* root){
  while (root) {
    root->left && f(root);
    root = root->right;
  }
}


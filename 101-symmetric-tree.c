/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool isSym(struct TreeNode *a, struct TreeNode *b) {
  return (!a && !b) ||
    (a && b &&
     a->val == b->val &&
     isSym(a->left, b->right) &&
     isSym(a->right, b->left));
}

bool isSymmetric(struct TreeNode* root){
  return !root || isSym(root->left, root->right);
}

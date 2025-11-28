# Problem: Balanced Binary Tree
# LeetCode URL: https://leetcode.com/problems/balanced-binary-tree/description/
# Description: Given a binary tree, determine if it is height-balanced.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if not root:
            return True

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        if not left_balanced or not right_balanced:
            return False

        return abs(self.height(root.left) - self.height(root.right)) <= 1

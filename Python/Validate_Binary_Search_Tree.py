# Problem: Validate Binary Search Tree
# LeetCode URL: https://leetcode.com/problems/validate-binary-search-tree/description/
# Description: Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# challenge

class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root, float("-inf"), float("inf"))